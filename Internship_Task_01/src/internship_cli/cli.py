import argparse


def greet(name):
    """Display a personalized welcome message."""
    print(f"Hello, {name}! Welcome to Student CLI Toolkit.")


def calculate(operation, a, b):
    """Perform basic arithmetic calculations."""

    try:
        if operation == "add":
            result = a + b

        elif operation == "subtract":
            result = a - b

        elif operation == "multiply":
            result = a * b

        elif operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero.")

            result = a / b

        print(f"Result: {result:g}")

    except ValueError as error:
        print(f"Error: {error}")
def show_info():
    """Display project information."""
    print("Student CLI Toolkit")
    print("Version: 1.0.0")
    print("Developed using Python 3.11.9")


def main():
    parser = argparse.ArgumentParser(
        description="Student CLI Toolkit"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # GREET COMMAND
    greet_parser = subparsers.add_parser(
        "greet",
        help="Greet a student"
    )

    greet_parser.add_argument(
        "--name",
        type=str,
        default="Student",
        help="Student name"
    )

    # CALCULATE COMMAND
    calc_parser = subparsers.add_parser(
        "calculate",
        help="Perform calculations"
    )

    calc_parser.add_argument(
        "--operation",
        choices=["add", "subtract", "multiply", "divide"],
        required=True,
        help="Mathematical operation"
    )

    calc_parser.add_argument(
        "--a",
        type=float,
        required=True,
        help="First number"
    )

    calc_parser.add_argument(
        "--b",
        type=float,
        required=True,
        help="Second number"
    )

    # INFO COMMAND
    subparsers.add_parser(
        "info",
        help="Display project information"
    )

    args = parser.parse_args()

    if args.command == "greet":
        greet(args.name)

    elif args.command == "calculate":
        calculate(args.operation, args.a, args.b)

    elif args.command == "info":
        show_info()


if __name__ == "__main__":
    main()