#!/bin/bash

venv/bin/pytest -m smoke_suite --html=smoke_test_suite_report.html
