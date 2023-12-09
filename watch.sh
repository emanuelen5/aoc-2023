#! /usr/bin/env bash

day="$1"

if [ ! -d "$day" ]; then
    echo "'$day' is not a folder" >&2
    exit 1
fi

do_break=false
trap 'do_break=true' SIGINT

while true; do
    git ls-files "$day" | \
    entr -cd \
    ./run.sh "$day"

    $do_break && break;

    sleep 1
done
