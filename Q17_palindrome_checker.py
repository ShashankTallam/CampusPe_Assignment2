

def palindrome_checker():
    try:
        # Step 1: Take input from user
        user_input = input("Enter word/number: ")

        # Step 2: Reverse the input using slicing
        reversed_input = user_input[::-1]

        print("Original:", user_input)
        print("Reversed:", reversed_input)

        # Step 3: Compare lowercase versions 
        if user_input.lower() == reversed_input.lower():
            print("Result: PALINDROME")
        else:
            print("Result: NOT PALINDROME")

    except Exception:
        print("Invalid input.")
#calling the function
palindrome_checker()