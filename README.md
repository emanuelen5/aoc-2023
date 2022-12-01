# Advent of Code 2023

## Creating a template for a new day
Create a template directory for a specific date, with a simple standard format with template for unit tests and main solution:

```bash
./create_day 3
```

This will create a branch called `day/3`, and a git commit with the template created.

## Running
Run unit tests and solution for a specific day:

```bash
./run day3
```

### Watch
Or, for convenience, you can watch the files during development using something like this:

```bash
ls */*.py */data/*.txt | entr -c ./run.sh day3
```
