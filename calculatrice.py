import math

# Trigonometric functions
def sin_angel(x):
    y = math.radians(x)  # Convert degrees to radians
    return math.sin(y)

def cos_angel(x):
    y = math.radians(x)  # Convert degrees to radians
    return math.cos(y)

# Basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

# Main program
def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Exit")

    while True:
        try:
            choice = int(input("\nEnter the number corresponding to your choice: "))
            if choice == 7:
                print("Thank you for using the calculator. Goodbye!")
                break
            elif choice in [1, 2, 3, 4]:  # Arithmetic operations
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                if choice == 1:
                    print(f"The result is: {add(a, b)}")
                elif choice == 2:
                    print(f"The result is: {subtract(a, b)}")
                elif choice == 3:
                    print(f"The result is: {multiply(a, b)}")
                elif choice == 4:
                    print(f"The result is: {divide(a, b)}")
            elif choice in [5, 6]:  # Trigonometric functions
                angle = float(input("Enter the angle in degrees: "))
                if choice == 5:
                    print(f"The sine of {angle} degrees is: {sin_angel(angle)}")
                elif choice == 6:
                    print(f"The cosine of {angle} degrees is: {cos_angel(angle)}")
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the calculator
calculator()

