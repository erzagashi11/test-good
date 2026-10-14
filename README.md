# Gradebook

Small command-line tool that reads course grades from a CSV file and prints a
ranked report with weighted scores and letter grades.

## Run

    python main.py data/grades.csv

The CSV needs the columns `name,homework,midterm,final`, each score 0-100.
The final score weighs homework 30%, midterm 30% and final exam 40%.

## Test

    python -m unittest discover -s tests -t .

Only the standard library is used; there are no dependencies to install.
