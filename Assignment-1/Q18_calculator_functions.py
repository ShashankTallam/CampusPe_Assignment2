
def add(a, b):
    return a + b

# Returns difference of two numbers
def subtract(a, b):
    return a - b

# Returns product of two numbers
def multiply(a, b):
    return a * b

# Returns division result, with zero-division check
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Returns remainder, with zero-division check
def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b


def power(a, b):
    return a ** b

# Main calculator function 
def calculator():
    
    while True:
        print("\n===== FUNCTION CALCULATOR =====")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Power\n7. Exit")

        try:
            # Take operation choice from user
            choice = int(input("Enter choice: "))

            # Exit condition
            if choice == 7:
                print("Exiting calculator.")
                break

            # Take two numbers for selected operation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Call respective function based on menu choice
            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))
            elif choice == 5:
                print("Result:", modulus(num1, num2))
            elif choice == 6:
                print("Result:", power(num1, num2))
            else:
                print("Invalid choice.")

        # Handles invalid inputs 
        except Exception:
            print("Invalid input.")

# calling the function
calculator()