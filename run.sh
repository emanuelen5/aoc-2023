#!/usr/bin/env bash

day="$1"
shift

run_prod=true
for arg in "$@"; do
    case $arg in
        --skip-prod*)
            run_prod=false
        ;;
        *)
            # unknown option
        ;;
    esac
done

python3 -m unittest discover "$day" && echo "Tests passed"

if $run_prod; then
    python3 -m "$day"
fi
