#!/bin/bash
set -eo pipefail

day=$1

if [ -z "$day" ]; then
  echo "please provide day number. eg: 3"
  exit 1
fi

cp -R template $day

pushd $day > /dev/null

curl -s -b "session=$AOC_SESSION" https://adventofcode.com/2022/day/$day/input -o input.txt

popd > /dev/null
