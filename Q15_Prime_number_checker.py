
def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False

    # Check divisibility 
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Main function 
def prime_program():
    try:
        # Take one number and tell whether it is prime or not
        number = int(input("Enter a number: "))

        if is_prime(number):
            print(number, "is PRIME")
        else:
            print(number, "is NOT PRIME")

        # Take range input from user
        start = int(input("Enter start range: "))
        end = int(input("Enter end range: "))

        # Collect all prime numbers in the given range
        primes = []
        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(num)

        # Display the final list 
        print("Prime numbers:", primes)

    # Handles invalid inputs
    except Exception:
        print("Invalid input.")

# calling the function
prime_program()