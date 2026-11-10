# Student CLI Toolkit

A Python-based Command-Line Interface (CLI) application developed as part of Internship Task 1.

## 1. Project Overview

Student CLI Toolkit is a simple command-line application that demonstrates Python command-line argument parsing, subcommands, input validation, error handling, and automated testing.

## 2. Features

- Personalized student greeting
- Basic arithmetic operations
- Project information display
- Command-line help
- Input validation using argparse
- Error handling for division by zero
- Automated tests using pytest

## 3. Technologies Used

- Python 3.11.9
- Pipenv
- argparse
- pytest
- setuptools

## 4. Project Structure

Internship_Task_01/
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── pyproject.toml
├── README.md
├── screenshots/
├── src/
│   └── internship_cli/
│       ├── __init__.py
│       └── cli.py
└── tests/
    └── test_cli.py


## 5. Installation

Clone or download the project.
Install dependencies:
>>>python -m pipenv install --dev

Install the application:
>>>python -m pipenv install -e .

## 6. Usage

Greeting
>>>python -m pipenv run internship-cli greet --name Siva

Addition
>>>python -m pipenv run internship-cli calculate --operation add --a 10 --b 20

Subtraction
>>>python -m pipenv run internship-cli calculate --operation subtract --a 30 --b 10

Multiplication
>>>python -m pipenv run internship-cli calculate --operation multiply --a 5 --b 4

Division
>>>python -m pipenv run internship-cli calculate --operation divide --a 20 --b 5

Project Information
>>>python -m pipenv run internship-cli info

Help
>>>python -m pipenv run internship-cli --help

## 7. Testing

Run automated tests:
>>>python -m pipenv run pytest -v

## 8. Error Handling

The application handles:

- Invalid mathematical operations
- Invalid numeric arguments
- Division by zero
- Missing commands

## 9. Learning Outcomes

- Python project setup
- Virtual environment management
- Command-line argument parsing
- CLI application development
- Error handling
- Automated testing

## 10. Version

**Version:** 1.0.0