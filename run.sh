#!/usr/bin/env bash

day="$1"
cd "$day" || exit 1

cargo test && echo "Tests passed"
cargo run
