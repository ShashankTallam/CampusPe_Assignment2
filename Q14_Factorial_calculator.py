
def factorial_calculator():
    try:
        # integer input from user
        number = int(input("Enter number: "))

        
        if number < 0:
            print("Factorial not defined for negative numbers.")
            return

        # Start factorial with 1 
        factorial = 1

        
        steps = ""

        # Multiply from number down to 1
        for i in range(number, 0, -1):
            factorial *= i
            steps += str(i)

            # Add 'x' between numbers
            if i != 1:
                steps += " x "

        # Print final result 
        print(f"{number}! = {steps} = {factorial}")

    # Handles invalid inputs 
    except Exception:
        print("Invalid input.")

# calling the function
factorial_calculator()