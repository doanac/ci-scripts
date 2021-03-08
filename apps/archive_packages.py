#!/usr/bin/python3
# Copyright (c) 2021 Foundries.io
# SPDX-License-Identifier: Apache-2.0
import argparse
import json
import os
import subprocess
import sys
from tempfile import mkstemp
from typing import List, NamedTuple

script = """#!/bin/sh -e

if [ -f /lib/apk/db/installed ] ; then
    echo "!APK!"
    cat /lib/apk/db/installed
    exit 0
fi

if [ -f /var/lib/dpkg/status ] ; then
    echo "!DEB!"
    cat /var/lib/dpkg/status
    exit 0
fi

if [ -e /usr/bin/rpm ] ; then
    # rpm db is berkleyDB for fedora < 33 and sqlite after
    # just use the tooling for this one
    echo "!RPM!"
    rpm -qa --qf '%{NAME}\t%{VERSION}\n'
    exit 0
fi

exit 1
"""


class Package(NamedTuple):
    name: str
    vers: str


def _apk_versions(lines: List[str]) -> List[Package]:
    packages: List[Package] = []
    p = v = None
    for line in lines:
        if not line:
            if p and v:
                packages.append(Package(p, v))
            # new package
            p = v = None
        elif line[:2] == "P:":
            p = line[2:]
        elif line[:2] == "V:":
            v = line[2:]
    if p and v:
        packages.append(Package(p, v))
    return packages


def _deb_versions(lines: List[str]) -> List[str]:
    packages: List[Package] = []
    p = v = None
    for line in lines:
        if not line:
            if p and v:
                packages.append(Package(p, v))
            # new package
            p = v = None
        elif line.startswith("Package:"):
            p = line[9:]
        elif line.startswith("Version:"):
            v = line[9:]
    if p and v:
        packages.append(Package(p, v))
    return packages


def _rpm_versions(lines: List[str]) -> List[str]:
    packages: List[Package] = []
    for line in lines:
        p, v = line.split()
        packages.append(Package(p, v))
    return packages


def list_versions(container: str) -> List[str]:
    f, tempfile = mkstemp()
    os.write(f, script.encode())
    os.fchmod(f, 0o755)
    os.close(f)

    try:
        args = [
            "docker",
            "run",
            "--rm",
            "--entrypoint=/fio_list",
            "-v",
            tempfile + ":/fio_list:ro",
            container,
        ]
        out = subprocess.check_output(args)
    finally:
        os.unlink(tempfile)

    lines = out.decode().splitlines()
    if lines[0] == "!APK!":
        return _apk_versions(lines[1:])
    elif lines[0] == "!DEB!":
        return _deb_versions(lines[1:])
    elif lines[0] == "!RPM!":
        return _rpm_versions(lines[1:])
    raise ValueError("Unable to find package listing in " + "\n".join(lines))


def main():
    parser = argparse.ArgumentParser(
        "Extract installed package information from container as json"
    )
    parser.add_argument("--append", action="store_true", help="Append to file if it exists")
    parser.add_argument("container")
    parser.add_argument("outfile")

    args = parser.parse_args()
    idx = args.container.find("@sha256")
    if idx > 0:
        container_name = args.container[:idx]
    else:
        container_name = args.container.split(":")[0]

    data = {
        "packages": {x.name: {"version": x.vers} for x in list_versions(args.container)}
    }
    if args.outfile == "-":
        json.dump(data, sys.stdout, indent=2)
    else:
        cur = {}
        if args.append:
            try:
                with open(args.outfile) as f:
                    cur = json.load(f)
            except FileNotFoundError:
                pass
        cur[container_name] = data
        with open(args.outfile, "w") as f:
            json.dump(cur, f)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise
        sys.exit(e)
