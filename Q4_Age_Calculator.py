


def age_calculator():
    try:
        # Step 1: Take birth year input
        birth_year = int(input("Enter your birth year: "))
        current_year = 2026  

        # Step 2: Calculate current age
        current_age = current_year - birth_year

        if current_age < 0:
            print("Birth year cannot be in the future.")
            return

        print("\n===== AGE DETAILS =====")
        print("Current Age:", current_age)
        print("Age in months:", current_age * 12)
        print("Age in days (approx):", current_age * 365)
        print("Age in hours:", current_age * 365 * 24)
        print("Age in minutes:", current_age * 365 * 24 * 60)
        print("Years until 100:", 100 - current_age)

    except ValueError:
        print("Invalid input! Please enter a valid year.")
#calling the function
age_calculator()