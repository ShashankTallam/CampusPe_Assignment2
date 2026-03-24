
def string_manipulator():

    try:
        # Step 1: Take sentence input from the user
        user_sentence = input("Enter a sentence: ")

        # Step 2: Split sentence into words using space
        word_list = user_sentence.split()

        print("\n===== STRING ANALYSIS =====")

        # Step 3: Print original sentence
        print("Original Sentence:", user_sentence)

        # Step 4: Count total characters including spaces
        characters_with_spaces = len(user_sentence)
        print("Total characters (with spaces):", characters_with_spaces)

        # Step 5: Count total characters excluding spaces
        characters_without_spaces = len(user_sentence.replace(" ", ""))
        print("Total characters (without spaces):", characters_without_spaces)

        # Step 6: Count total words
        total_words = len(word_list)
        print("Total words:", total_words)

        # Step 7: Convert to uppercase
        print("UPPERCASE:", user_sentence.upper())

        # Step 8: Convert to lowercase
        print("lowercase:", user_sentence.lower())

        # Step 9: Convert to title case
        print("Title Case:", user_sentence.title())

        # Step 10: Print first and last word if sentence is not empty
        if total_words > 0:
            print("First word:", word_list[0])
            print("Last word:", word_list[-1])
        else:
            print("No words entered.")

        # Step 11: Reverse the sentence
        reversed_sentence = user_sentence[::-1]
        print("Reversed Sentence:", reversed_sentence)

    except Exception as error:
        # Catch unexpected errors
        print("Something went wrong:", error)


# Calling the function
string_manipulator()