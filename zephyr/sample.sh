#!/bin/bash -e

HERE=$(dirname $(readlink -f $0))
source $HERE/../helpers.sh
require_params PLATFORM APP

run pip3 install -U west

status "Compiling $APP ..."
source ./zephyr-env.sh
mkdir build
cd build
cmake -GNinja -DBOARD=$PLATFORM ../$APP
ninja
