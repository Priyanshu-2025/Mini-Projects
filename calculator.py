"""
Calculator Program (CLI)
------------------------
Operations:
- Addition, Subtraction, Multiplication, Division (with zero handling)
- Power (x^y), Square Root, Percentage
- History of last results (in-memory)
"""

import math
from typing import List, Callable, Tuple


def read_float(prompt: str) -> float:
    """Safely read a float from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number. Try again.")


def binary_op(op_name: str, func: Callable[[float, float], float]) -> float:
    """Handle binary operations (need two numbers)."""
    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    try:
        result = func(a, b)
    except ZeroDivisionError:
        print("❌ Division by zero is not allowed.")
        return math.nan
    print(f"✅ {op_name} result: {result}")
    return result


def unary_op(op_name: str, func: Callable[[float], float]) -> float:
    """Handle unary operations (need one number)."""
    x = read_float("Enter number: ")
    try:
        result = func(x)
    except ValueError:
        print("❌ Domain error (e.g., sqrt of negative).")
        return math.nan
    print(f"✅ {op_name} result: {result}")
    return result


def percentage(base: float, pct: float) -> float:
    """pct % of base."""
    return (pct / 100.0) * base


def menu() -> None:
    history: List[float] = []

    actions: List[Tuple[str, Callable[[], float]]] = [
        ("Add", lambda: binary_op("Addition", lambda x, y: x + y)),
        ("Subtract", lambda: binary_op("Subtraction", lambda x, y: x - y)),
        ("Multiply", lambda: binary_op("Multiplication", lambda x, y: x * y)),
        ("Divide", lambda: binary_op("Division", lambda x, y: x / y)),
        ("Power (x^y)", lambda: binary_op("Power", lambda x, y: x ** y)),
        ("Square Root", lambda: unary_op("Square Root", math.sqrt)),
        ("Percentage (pct% of base)", lambda: (
            lambda base, pct: print(f"✅ Percentage result: {percentage(base, pct)}") or percentage(base, pct)
        )(
            read_float("Base: "), read_float("Percent (%): ")
        )),
    ]

    print("🧮 Welcome to the Calculator!")
    while True:
        print("\n--- Calculator Menu ---")
        for i, (name, _) in enumerate(actions, start=1):
            print(f"{i}. {name}")
        print(f"{len(actions) + 1}. Show History")
        print(f"{len(actions) + 2}. Clear History")
        print(f"{len(actions) + 3}. Exit")

        choice = input("Choose an option: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(actions):
                _, fn = actions[idx - 1]
                res = fn()
                if not math.isnan(res):
                    history.append(res)
            elif idx == len(actions) + 1:
                print("📜 History:", history if history else "No results yet.")
            elif idx == len(actions) + 2:
                history.clear()
                print("🧹 History cleared.")
            elif idx == len(actions) + 3:
                print("👋 Bye!")
                break
            else:
                print("❌ Invalid choice.")
        else:
            print("❌ Enter a number corresponding to the menu.")


if __name__ == "__main__":
    menu()