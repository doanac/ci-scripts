#!/usr/bin/env python3
# Copyright (c) 2021 Foundries.io
# SPDX-License-Identifier: Apache-2.0

import os
import json
import subprocess
import unittest


class TestArchivePackages(unittest.TestCase):
    def setUp(self):
        here = os.path.dirname(os.path.abspath(__file__))
        os.chdir(here)

    def test_alpine(self):
        out = subprocess.check_output(
            [
                "../apps/archive_packages.py",
                "alpine@sha256:a75afd8b57e7f34e4dad8d65e2c7ba2e1975c795ce1ee22fa34f8cf46f96a3be",
                "-",
            ]
        )
        expected = {
            "musl": {"version": "1.2.2-r0"},
            "busybox": {"version": "1.32.1-r3"},
            "alpine-baselayout": {"version": "3.2.0-r8"},
            "alpine-keys": {"version": "2.2-r0"},
            "libcrypto1.1": {"version": "1.1.1j-r0"},
            "libssl1.1": {"version": "1.1.1j-r0"},
            "ca-certificates-bundle": {"version": "20191127-r5"},
            "libtls-standalone": {"version": "2.9.1-r1"},
            "ssl_client": {"version": "1.32.1-r3"},
            "zlib": {"version": "1.2.11-r3"},
            "apk-tools": {"version": "2.12.1-r0"},
            "scanelf": {"version": "1.2.8-r0"},
            "musl-utils": {"version": "1.2.2-r0"},
            "libc-utils": {"version": "0.7.2-r3"},
        }
        found = json.loads(out.decode())
        self.assertEqual(expected, found["packages"])

    def test_deb(self):
        out = subprocess.check_output(
            [
                "../apps/archive_packages.py",
                "ubuntu@sha256:b4f9e18267eb98998f6130342baacaeb9553f136142d40959a1b46d6401f0f2b",
                "-",
            ]
        )
        expected = {
            "adduser": {"version": "3.118ubuntu2"},
            "apt": {"version": "2.0.4"},
            "base-files": {"version": "11ubuntu5.3"},
            "base-passwd": {"version": "3.5.47"},
            "bash": {"version": "5.0-6ubuntu1.1"},
            "bsdutils": {"version": "1:2.34-0.1ubuntu9.1"},
            "bzip2": {"version": "1.0.8-2"},
            "coreutils": {"version": "8.30-3ubuntu2"},
            "dash": {"version": "0.5.10.2-6"},
            "debconf": {"version": "1.5.73"},
            "debianutils": {"version": "4.9.1"},
            "diffutils": {"version": "1:3.7-3"},
            "dpkg": {"version": "1.19.7ubuntu3"},
            "e2fsprogs": {"version": "1.45.5-2ubuntu1"},
            "fdisk": {"version": "2.34-0.1ubuntu9.1"},
            "findutils": {"version": "4.7.0-1ubuntu1"},
            "gcc-10-base": {"version": "10.2.0-5ubuntu1~20.04"},
            "gpgv": {"version": "2.2.19-3ubuntu2.1"},
            "grep": {"version": "3.4-1"},
            "gzip": {"version": "1.10-0ubuntu4"},
            "hostname": {"version": "3.23"},
            "init-system-helpers": {"version": "1.57"},
            "libacl1": {"version": "2.2.53-6"},
            "libapt-pkg6.0": {"version": "2.0.4"},
            "libattr1": {"version": "1:2.4.48-5"},
            "libaudit-common": {"version": "1:2.8.5-2ubuntu6"},
            "libaudit1": {"version": "1:2.8.5-2ubuntu6"},
            "libblkid1": {"version": "2.34-0.1ubuntu9.1"},
            "libbz2-1.0": {"version": "1.0.8-2"},
            "libc-bin": {"version": "2.31-0ubuntu9.2"},
            "libc6": {"version": "2.31-0ubuntu9.2"},
            "libcap-ng0": {"version": "0.7.9-2.1build1"},
            "libcom-err2": {"version": "1.45.5-2ubuntu1"},
            "libcrypt1": {"version": "1:4.4.10-10ubuntu4"},
            "libdb5.3": {"version": "5.3.28+dfsg1-0.6ubuntu2"},
            "libdebconfclient0": {"version": "0.251ubuntu1"},
            "libext2fs2": {"version": "1.45.5-2ubuntu1"},
            "libfdisk1": {"version": "2.34-0.1ubuntu9.1"},
            "libffi7": {"version": "3.3-4"},
            "libgcc-s1": {"version": "10.2.0-5ubuntu1~20.04"},
            "libgcrypt20": {"version": "1.8.5-5ubuntu1"},
            "libgmp10": {"version": "2:6.2.0+dfsg-4"},
            "libgnutls30": {"version": "3.6.13-2ubuntu1.3"},
            "libgpg-error0": {"version": "1.37-1"},
            "libhogweed5": {"version": "3.5.1+really3.5.1-2"},
            "libidn2-0": {"version": "2.2.0-2"},
            "liblz4-1": {"version": "1.9.2-2"},
            "liblzma5": {"version": "5.2.4-1ubuntu1"},
            "libmount1": {"version": "2.34-0.1ubuntu9.1"},
            "libncurses6": {"version": "6.2-0ubuntu2"},
            "libncursesw6": {"version": "6.2-0ubuntu2"},
            "libnettle7": {"version": "3.5.1+really3.5.1-2"},
            "libp11-kit0": {"version": "0.23.20-1ubuntu0.1"},
            "libpam-modules": {"version": "1.3.1-5ubuntu4.1"},
            "libpam-modules-bin": {"version": "1.3.1-5ubuntu4.1"},
            "libpam-runtime": {"version": "1.3.1-5ubuntu4.1"},
            "libpam0g": {"version": "1.3.1-5ubuntu4.1"},
            "libpcre2-8-0": {"version": "10.34-7"},
            "libpcre3": {"version": "2:8.39-12build1"},
            "libprocps8": {"version": "2:3.3.16-1ubuntu2"},
            "libseccomp2": {"version": "2.4.3-1ubuntu3.20.04.3"},
            "libselinux1": {"version": "3.0-1build2"},
            "libsemanage-common": {"version": "3.0-1build2"},
            "libsemanage1": {"version": "3.0-1build2"},
            "libsepol1": {"version": "3.0-1"},
            "libsmartcols1": {"version": "2.34-0.1ubuntu9.1"},
            "libss2": {"version": "1.45.5-2ubuntu1"},
            "libstdc++6": {"version": "10.2.0-5ubuntu1~20.04"},
            "libsystemd0": {"version": "245.4-4ubuntu3.4"},
            "libtasn1-6": {"version": "4.16.0-2"},
            "libtinfo6": {"version": "6.2-0ubuntu2"},
            "libudev1": {"version": "245.4-4ubuntu3.4"},
            "libunistring2": {"version": "0.9.10-2"},
            "libuuid1": {"version": "2.34-0.1ubuntu9.1"},
            "libzstd1": {"version": "1.4.4+dfsg-3"},
            "login": {"version": "1:4.8.1-1ubuntu5.20.04"},
            "logsave": {"version": "1.45.5-2ubuntu1"},
            "lsb-base": {"version": "11.1.0ubuntu2"},
            "mawk": {"version": "1.3.4.20200120-2"},
            "mount": {"version": "2.34-0.1ubuntu9.1"},
            "ncurses-base": {"version": "6.2-0ubuntu2"},
            "ncurses-bin": {"version": "6.2-0ubuntu2"},
            "passwd": {"version": "1:4.8.1-1ubuntu5.20.04"},
            "perl-base": {"version": "5.30.0-9ubuntu0.2"},
            "procps": {"version": "2:3.3.16-1ubuntu2"},
            "sed": {"version": "4.7-1"},
            "sensible-utils": {"version": "0.0.12+nmu1"},
            "sysvinit-utils": {"version": "2.96-2.1ubuntu1"},
            "tar": {"version": "1.30+dfsg-7ubuntu0.20.04.1"},
            "ubuntu-keyring": {"version": "2020.02.11.2"},
            "util-linux": {"version": "2.34-0.1ubuntu9.1"},
            "zlib1g": {"version": "1:1.2.11.dfsg-2ubuntu1.2"},
        }
        found = json.loads(out.decode())
        self.assertEqual(expected, found["packages"])

    def test_rpm(self):
        out = subprocess.check_output(
            [
                "../apps/archive_packages.py",
                "fedora@sha256:3738909921e6d370a5c8dea69951b66af69264ba6b4bc270c856a682d11d5542",
                "-",
            ]
        )
        expected = {
            "libgcc": {"version": "10.2.1"},
            "crypto-policies": {"version": "20200918"},
            "tzdata": {"version": "2021a"},
            "fedora-release-identity-container": {"version": "33"},
            "pcre2-syntax": {"version": "10.36"},
            "libreport-filesystem": {"version": "2.14.0"},
            "dnf-data": {"version": "4.5.2"},
            "fedora-gpg-keys": {"version": "33"},
            "fedora-release-container": {"version": "33"},
            "fedora-repos": {"version": "33"},
            "fedora-release-common": {"version": "33"},
            "setup": {"version": "2.13.7"},
            "filesystem": {"version": "3.14"},
            "basesystem": {"version": "11"},
            "coreutils-common": {"version": "8.32"},
            "python-setuptools-wheel": {"version": "49.1.3"},
            "publicsuffix-list-dafsa": {"version": "20190417"},
            "ncurses-base": {"version": "6.2"},
            "bash": {"version": "5.0.17"},
            "ncurses-libs": {"version": "6.2"},
            "glibc-common": {"version": "2.32"},
            "glibc-minimal-langpack": {"version": "2.32"},
            "glibc": {"version": "2.32"},
            "zlib": {"version": "1.2.11"},
            "bzip2-libs": {"version": "1.0.8"},
            "xz-libs": {"version": "5.2.5"},
            "libzstd": {"version": "1.4.7"},
            "sqlite-libs": {"version": "3.34.1"},
            "libdb": {"version": "5.3.28"},
            "gmp": {"version": "6.2.0"},
            "libcom_err": {"version": "1.45.6"},
            "libxcrypt": {"version": "4.4.17"},
            "popt": {"version": "1.18"},
            "libcap": {"version": "2.48"},
            "libgpg-error": {"version": "1.41"},
            "libuuid": {"version": "2.36.1"},
            "libxml2": {"version": "2.9.10"},
            "readline": {"version": "8.0"},
            "lua-libs": {"version": "5.4.2"},
            "file-libs": {"version": "5.39"},
            "elfutils-libelf": {"version": "0.182"},
            "expat": {"version": "2.2.8"},
            "libattr": {"version": "2.4.48"},
            "libacl": {"version": "2.2.53"},
            "libffi": {"version": "3.1"},
            "p11-kit": {"version": "0.23.22"},
            "libunistring": {"version": "0.9.10"},
            "libidn2": {"version": "2.3.0"},
            "libsmartcols": {"version": "2.36.1"},
            "libstdc++": {"version": "10.2.1"},
            "libassuan": {"version": "2.5.3"},
            "libgcrypt": {"version": "1.8.7"},
            "alternatives": {"version": "1.14"},
            "json-c": {"version": "0.14"},
            "libcap-ng": {"version": "0.8"},
            "audit-libs": {"version": "3.0.1"},
            "libsepol": {"version": "3.1"},
            "libtasn1": {"version": "4.16.0"},
            "p11-kit-trust": {"version": "0.23.22"},
            "lz4-libs": {"version": "1.9.1"},
            "keyutils-libs": {"version": "1.6.1"},
            "pcre": {"version": "8.44"},
            "grep": {"version": "3.4"},
            "pcre2": {"version": "10.36"},
            "libselinux": {"version": "3.1"},
            "sed": {"version": "4.8"},
            "openssl-libs": {"version": "1.1.1i"},
            "coreutils": {"version": "8.32"},
            "ca-certificates": {"version": "2020.2.41"},
            "libblkid": {"version": "2.36.1"},
            "libmount": {"version": "2.36.1"},
            "glib2": {"version": "2.66.7"},
            "systemd-libs": {"version": "246.10"},
            "zchunk-libs": {"version": "1.1.9"},
            "libusbx": {"version": "1.0.24"},
            "libfdisk": {"version": "2.36.1"},
            "python-pip-wheel": {"version": "20.2.2"},
            "gzip": {"version": "1.10"},
            "cracklib": {"version": "2.9.6"},
            "libarchive": {"version": "3.5.1"},
            "libsemanage": {"version": "3.1"},
            "shadow-utils": {"version": "4.8.1"},
            "libutempter": {"version": "1.2.1"},
            "vim-minimal": {"version": "8.2.2488"},
            "libpsl": {"version": "0.21.1"},
            "libcomps": {"version": "0.1.15"},
            "libmetalink": {"version": "0.1.3"},
            "libksba": {"version": "1.3.5"},
            "mpfr": {"version": "4.1.0"},
            "nettle": {"version": "3.6"},
            "gnutls": {"version": "3.6.15"},
            "libeconf": {"version": "0.3.8"},
            "libsigsegv": {"version": "2.11"},
            "gawk": {"version": "5.1.0"},
            "libverto": {"version": "0.3.0"},
            "krb5-libs": {"version": "1.18.2"},
            "libtirpc": {"version": "1.2.6"},
            "libnsl2": {"version": "1.2.0"},
            "libpwquality": {"version": "1.4.4"},
            "pam": {"version": "1.4.0"},
            "cyrus-sasl-lib": {"version": "2.1.27"},
            "openldap": {"version": "2.4.50"},
            "libyaml": {"version": "0.2.5"},
            "npth": {"version": "1.6"},
            "gnupg2": {"version": "2.2.25"},
            "gpgme": {"version": "1.14.0"},
            "gdbm-libs": {"version": "1.19"},
            "python3": {"version": "3.9.1"},
            "python3-libs": {"version": "3.9.1"},
            "python3-libcomps": {"version": "0.1.15"},
            "python3-gpg": {"version": "1.14.0"},
            "libbrotli": {"version": "1.0.9"},
            "libgomp": {"version": "10.2.1"},
            "libnghttp2": {"version": "1.43.0"},
            "libsss_idmap": {"version": "2.4.1"},
            "libsss_nss_idmap": {"version": "2.4.1"},
            "elfutils-default-yama-scope": {"version": "0.182"},
            "elfutils-libs": {"version": "0.182"},
            "libssh-config": {"version": "0.9.5"},
            "libssh": {"version": "0.9.5"},
            "libcurl": {"version": "7.71.1"},
            "curl": {"version": "7.71.1"},
            "rpm": {"version": "4.16.1.2"},
            "rpm-libs": {"version": "4.16.1.2"},
            "libmodulemd": {"version": "2.12.0"},
            "libsolv": {"version": "0.7.17"},
            "rpm-build-libs": {"version": "4.16.1.2"},
            "librepo": {"version": "1.12.1"},
            "libdnf": {"version": "0.55.2"},
            "python3-libdnf": {"version": "0.55.2"},
            "python3-hawkey": {"version": "0.55.2"},
            "tpm2-tss": {"version": "3.0.3"},
            "ima-evm-utils": {"version": "1.3.2"},
            "rpm-sign-libs": {"version": "4.16.1.2"},
            "python3-rpm": {"version": "4.16.1.2"},
            "python3-dnf": {"version": "4.5.2"},
            "dnf": {"version": "4.5.2"},
            "yum": {"version": "4.5.2"},
            "sssd-client": {"version": "2.4.1"},
            "sudo": {"version": "1.9.5p2"},
            "util-linux": {"version": "2.36.1"},
            "tar": {"version": "1.32"},
            "fedora-repos-modular": {"version": "33"},
            "rootfiles": {"version": "8.1"},
            "gpg-pubkey": {"version": "9570ff31"},
        }
        found = json.loads(out.decode())
        self.assertEqual(expected, found["packages"])


if __name__ == "__main__":
    unittest.main()