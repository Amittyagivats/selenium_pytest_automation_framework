![CiCD workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)
# Google Finance Test Framework

## Overview

This is a pytest-based test framework for automating tests on the https://www.google.com/finance website. The framework utilizes Selenium for web automation and follows the Page Object Model (POM) structure.

## Project Structure
google_test/
|-- tests/
|   |-- pages/
|   |   |-- __init__.py
|   |   |-- base_page.py
|   |   |-- home_page.py
|   |-- conftest.py
|   |-- test_finance_website.py
|-- pytest.ini
|-- requirements.txt
|-- README.md


- `conftest.py`: Configuration file for pytest fixtures.
- `pages`: Implements the Page Object Model (POM) structure.
- `tests/`: Directory containing test modules.
- `pytest.ini`: Configuration file for pytest.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.


## Test Cases

The test suite includes the following test modules:

- `test_finance_website.py`: All Tests for the website.

## Running Tests

- Install required packages:  `pip install -r requirements.txt`
- For Setting log level go in pytest.ini and set `log_file_level`
- Run all tests with HTML Report: `pytest --html=test_report.html`
- Run smoke-suite tests only: `./run_smoke_suite.sh`

## View the HTML Report
- Use xdg-open command to open html report: `xdg-open path/to/test_report.html`

## Checking Format of code
- Use below tool to check code according PEP8: Pylint, Black, autopep8

