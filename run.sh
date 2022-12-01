#!/usr/bin/env bash

day="$1"

python3 -m unittest discover "$day" && echo "Tests passed"
python3 -m "$day"
