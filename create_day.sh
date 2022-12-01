#!/usr/bin/env bash

set -x

dir="day$1"
if [ -d "$dir" ]; then
    echo "Directory '$dir' already created" >&2
    exit 1
fi

branch="day/$1"
if ! git branch "$branch"; then
    echo "Branch '$branch' does already exist. Clean up first and delete it to be able to initialize" >&2
    exit 1
fi
git checkout "$branch"

cp -r template/ "$dir"

read -rp "Paste input data into '$dir/data/input.txt' and '$dir/data/test_input.txt' and then press Enter to continue... "

git add "$dir"
git commit -m "Creating $dir from template"
