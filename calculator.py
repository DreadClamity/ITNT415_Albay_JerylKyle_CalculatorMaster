import os
import sys

class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"

WIDTH = 42

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print(Color.CYAN + Color.BOLD + "╔" + "═" * WIDTH + "╗")
    print("║" + "CALCULATOR MASTER".center(WIDTH) + "║")
    print("╚" + "═" * WIDTH + "╝" + Color.RESET)

def print_menu():
    options = [
        ("1", "Add", "+"),
        ("2", "Subtract", "-"),
        ("3", "Multiply", "×"),
        ("4", "Divide", "÷"),
        ("5", "Exit", "×"),
    ]
    print()
    for key, label, symbol in options:
        color = Color.RED if key == "5" else Color.GREEN
        print(f"  {Color.YELLOW}{key}{Color.RESET}  {color}{symbol}{Color.RESET}  {label}")
    print(Color.DIM + "─" * (WIDTH + 2) + Color.RESET)

def get_number(prompt):
    while True:
        raw = input(f"  {Color.BLUE}{prompt}{Color.RESET} ").strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  {Color.RED}✗ Please enter a valid number.{Color.RESET}")

def show_result(a, op, b, result):
    print()
    print(f"  {Color.DIM}┌{'─' * (WIDTH - 2)}┐{Color.RESET}")
    print(f"  {Color.BOLD}{a:g} {op} {b:g} = {Color.GREEN}{result:g}{Color.RESET}")
    print(f"  {Color.DIM}└{'─' * (WIDTH - 2)}┘{Color.RESET}")
    input(f"\n  {Color.DIM}Press Enter to continue...{Color.RESET}")

def add():
    a = get_number("First number:")
    b = get_number("Second number:")
    show_result("The Sum of "a, "+", b, a + b)

def subtract():
    a = get_number("First number:")
    b = get_number("Second number:")
    show_result("The Difference of "a, "-", b, a - b)

def multiply():
    a = get_number("First number:")
    b = get_number("Second number:")
    show_result("The Product of "a, "×", b, a * b)

def divide():
    a = get_number("First number:")
    b = get_number("Second number:")
    try:
        result = a / b
        show_result("The Quotient of "a, "÷", b, result)
    except ZeroDivisionError:
        print(f"\n  {Color.RED}✗ Error: Cannot divide by zero.{Color.RESET}")
        input(f"\n  {Color.DIM}Press Enter to continue...{Color.RESET}")

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input(f"  {Color.MAGENTA}Select an operation (1-5):{Color.RESET} ").strip()

        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            clear_screen()
            print(f"{Color.CYAN}Goodbye!{Color.RESET}")
            sys.exit(0)
        else:
            print(f"\n  {Color.RED}✗ Invalid choice. Try again.{Color.RESET}")
            input(f"\n  {Color.DIM}Press Enter to continue...{Color.RESET}")

if __name__ == "__main__":
    main()
