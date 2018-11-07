#!/bin/bash
# This script is used to run MongoDB_performance_python program.

if [ ! $# -ge 2 ]; then
    echo "Ex. usage 0: $0 10 10"
    exit 1
fi

count=$1
average=$2

python ./src/main.py --count $count --count $average
