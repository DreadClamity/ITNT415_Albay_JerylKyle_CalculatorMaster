def add():
    print("\n--- Addition ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
def subtract():
    print("\n--- Subtraction ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1} - {num2} = {num1 - num2}")
def multiply(): pass
def divide(): pass

while True:
    print("\n--- Calculator Master ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Select an operation (1-5): ")
    
    if choice == '1': add()
    elif choice == '2': subtract()
    elif choice == '3': multiply()
    elif choice == '4': divide()
    elif choice == '5': break
    else: print("Invalid choice.")
