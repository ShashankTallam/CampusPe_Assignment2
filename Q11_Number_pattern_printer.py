

def number_pattern_printer():

    try:
        print("\nChoose Pattern (1-7)")
        print("1. Increasing Number Triangle")
        print("2. Repeated Row Number Triangle")
        print("3. Reverse Number Triangle")
        print("4. Palindrome Pyramid")
        print("5. Centered Number Pyramid")
        print("6. Floyd's Number Triangle")
        print("7. Hollow Number Square")
        pattern_choice = int(input("Enter pattern number: "))
        height = int(input("Enter height: "))

        print("\n===== OUTPUT =====")

        # Pattern 1
        if pattern_choice == 1:
            for i in range(1, height + 1):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()

        # Pattern 2
        elif pattern_choice == 2:
            for i in range(1, height + 1):
                for j in range(i):
                    print(i, end=" ")
                print()

        # Pattern 3
        elif pattern_choice == 3:
            for i in range(height, 0, -1):
                for j in range(i, 0, -1):
                    print(j, end=" ")
                print()

        # Pattern 4
        elif pattern_choice == 4:
            for i in range(1, height + 1):
                # Print leading spaces to center-align the pattern
                print(" " * (height - i), end="")
                # Increasing numbers
                for j in range(1, i + 1):
                    print(j, end="")
                # Decreasing numbers
                for j in range(i - 1, 0, -1):
                    print(j, end="")
                print()

        # Pattern 5
        elif pattern_choice == 5:
            for i in range(1, height + 1):
                spaces = " " * (height - i)
                numbers = " ".join(str(j) for j in range(1, i + 1))
                print(spaces + numbers)

        # Pattern 6
        elif pattern_choice == 6:
            current_number = 1
            for i in range(1, height + 1):
                for j in range(i):
                    print(current_number, end=" ")
                    current_number += 1
                print()

        # Pattern 7
        elif pattern_choice == 7:
            for i in range(1, height + 1):
                for j in range(1, height + 1):
                    if i == 1 or i == height or j == 1 or j == height:
                        print("1", end=" ")
                    else:
                        print(" ", end=" ")
                print()
        else:
            print("Invalid pattern choice.")

    except Exception:
        print("Invalid input.")
# calling the function
number_pattern_printer()