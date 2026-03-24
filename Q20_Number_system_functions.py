
def factorial(n):

    if n < 0: return "Invalid"

    # Start multiplication result with 1
    result = 1

    # Multiply numbers from 1 to n
    for i in range(1, n+1):
        result *= i
    return result

# Checks whether a number is prime
def is_prime(n):

    if n <= 1: return False

    # Check divisibility 
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Returns the nth Fibonacci number
def fibonacci(n):
    # First two Fibonacci values
    a, b = 0, 1

    # Generate sequence up to nth position
    for _ in range(n):
        a, b = b, a + b
    return a

# Returns sum of all digits of the number
def sum_digits(n): return sum(int(d) for d in str(abs(n)))

# Returns reversed number
def reverse_number(n): return int(str(n)[::-1])

# Checks whether number is an Armstrong number
def is_armstrong(n):
    # Number of digits determines power
    power = len(str(n))

    # Sum of each digit raised to the power
    return n == sum(int(d)**power for d in str(n))

# Finds GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Finds LCM using GCD relation
def lcm(a, b):
    return abs(a*b)//gcd(a,b)

# Checks whether number is perfect
def is_perfect(n):
    # Perfect number = sum of proper divisors equals the number
    return n == sum(i for i in range(1, n) if n % i == 0)

# Main menu function 
def math_menu():
    
    while True:
        # Display menu options clearly 
        print("\n===== NUMBER SYSTEM MENU =====")
        print("1. Factorial")
        print("2. Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        
        choice = input("Choose option: ")

        if choice == "10":
            break

        try:
            # For these options, only one number input is needed
            if choice in ["1","2","3","4","5","6","9"]:
                number = int(input("Enter number: "))

            
            if choice == "1":
                print("Factorial:", factorial(number))
            elif choice == "2":
                print("Prime:", is_prime(number))
            elif choice == "3":
                print("Fibonacci:", fibonacci(number))
            elif choice == "4":
                print("Sum of digits:", sum_digits(number))
            elif choice == "5":
                print("Reversed:", reverse_number(number))
            elif choice == "6":
                print("Armstrong:", is_armstrong(number))
            elif choice == "7":
                # GCD requires two numbers
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a,b))
            elif choice == "8":
                # LCM requires two numbers
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a,b))
            elif choice == "9":
                print("Perfect number:", is_perfect(number))
            else:
                
                print("Invalid option.")

        # Handles invalid inputs
        except ValueError:
            print("Invalid input.")

# calling the main menu function

math_menu()