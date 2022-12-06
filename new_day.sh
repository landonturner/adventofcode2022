#!/bin/bash
set -eo pipefail

day=$1

if [ -z "$day" ]; then
  echo "Usage: new_day.sh <day>"
  echo ""
  echo "  day  the day number to create"
  exit 1
fi

cp -R template $day

pushd $day > /dev/null

curl -s -b "session=$AOC_SESSION" https://adventofcode.com/2022/day/$day/input -o input.txt

popd > /dev/null
