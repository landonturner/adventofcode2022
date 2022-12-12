#!/bin/bash
set -eo pipefail

day=$1

if [ -z "$day" ]; then
  for d in $(ls | sort -V); do
    if [ "$d" == "README.md" ]; then
      break
    fi
    day=$((d+1))
  done
  echo "day not submitted as input. using day = $day"
fi

cp -R template $day

pushd $day > /dev/null

curl -s -b "session=$AOC_SESSION" https://adventofcode.com/2022/day/$day/input -o input.txt

popd > /dev/null

cd $day

open "https://adventofcode.com/2022/day/$day"
