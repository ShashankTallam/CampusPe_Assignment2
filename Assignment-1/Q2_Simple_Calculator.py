
def simple_calculator():
    
    try:
        # Step 1: Ask the user to enter two numbers
        # Using float so that decimal numbers are also accepted
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        print("\n===== CALCULATION RESULTS =====")

        # Step 2: Addition
        addition = first_number + second_number
        print(f"{first_number} + {second_number} = {addition}")

        # Step 3: Subtraction
        subtraction = first_number - second_number
        print(f"{first_number} - {second_number} = {subtraction}")

        # Step 4: Multiplication
        multiplication = first_number * second_number
        print(f"{first_number} * {second_number} = {multiplication}")

        # Step 5: Division
        # Before dividing, check if second number is not zero
        if second_number != 0:
            division = first_number / second_number
            print(f"{first_number} / {second_number} = {round(division, 2)}")
        else:
            print("Division not possible (cannot divide by zero).")

        # Step 6: Modulus
        if second_number != 0:
            modulus = first_number % second_number
            print(f"{first_number} % {second_number} = {modulus}")
        else:
            print("Modulus not possible (cannot divide by zero).")

        # Step 7: Exponentiation (Power)
        power = first_number ** second_number
        print(f"{first_number} ^ {second_number} = {power}")

    # Step 8: Handle invalid input (like letters instead of numbers)
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Calling the function so it executes
simple_calculator()