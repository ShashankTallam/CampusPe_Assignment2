


def leap_year_checker():
    try:
        #  input from the user 
        year_value = int(input("Enter year: "))

        # Leap year rule:
        # 1) Divisible by 4 and not divisible by 100, OR
        # 2) Divisible by 400
        if (year_value % 4 == 0 and year_value % 100 != 0) or (year_value % 400 == 0):
            print(year_value, "is a Leap Year.")
        else:
            print(year_value, "is NOT a Leap Year.")

    # Error Checker
    except Exception:
        print("Invalid input.")

# Calling the function 
leap_year_checker()