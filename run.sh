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

echo "****************************"
echo "Running unit-tests for $day"
python3 -m unittest discover "$day" && echo "Tests passed"
echo

if $run_prod; then
    echo "********************************"
    echo "Running production run for $day"
    python3 -m "$day"
else
    echo "Skipping production run..."
fi
