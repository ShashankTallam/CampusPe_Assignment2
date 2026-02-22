
def multiplication_table():
    try:
        number = int(input("Enter number: "))
        end_range = int(input("Enter range (end): "))

        print(f"\nMultiplication Table of {number}")
        for i in range(1, end_range + 1):
            print(f"{number} x {i} = {number * i}")

    except Exception:
        print("Invalid input.")

multiplication_table()