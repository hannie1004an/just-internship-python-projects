import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from internship_cli.cli import calculate, greet, show_info


def test_addition(capsys):
    calculate("add", 10, 20)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Result: 30"


def test_subtraction(capsys):
    calculate("subtract", 30, 10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Result: 20"


def test_multiplication(capsys):
    calculate("multiply", 5, 4)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Result: 20"


def test_division(capsys):
    calculate("divide", 20, 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Result: 4"


def test_division_by_zero(capsys):
    calculate("divide", 10, 0)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Error: Cannot divide by zero."


def test_greeting(capsys):
    greet("Siva")
    captured = capsys.readouterr()
    assert captured.out.strip() == (
        "Hello, Siva! Welcome to Student CLI Toolkit."
    )


def test_project_info(capsys):
    show_info()
    captured = capsys.readouterr()
    assert "Student CLI Toolkit" in captured.out