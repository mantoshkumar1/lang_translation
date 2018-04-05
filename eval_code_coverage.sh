#!/bin/sh

# This shell script is used to generate code coverage of this application.
# coverage commands are using .coveragerc to control coverage.py

echo 'Erasing previously collected coverage data'
coverage erase

echo 'Running Python testsuits and collecting execution data'
coverage run -m unittest discover

echo 'Producing annotated HTML listings with coverage results'
coverage html

echo 'Code coverage report has been opened in system default browser'
python -m webbrowser ./docs/coverage_html_report/index.html

echo 'GoodBye!'