
def count_words(text):
    return len(text.split())

# Counts vowels (a, e, i, o, u)
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

# Counts consonants 
def count_consonants(text):
    return sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")

# Reverses the full  string
def reverse_text(text):
    return text[::-1]

# Checks whether text is a palindrome 
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

# Removes all vowels from the text
def remove_vowels(text):
    return "".join(char for char in text if char.lower() not in "aeiou")

# Returns dictionary with each word 
def word_frequency(text):
    words = text.lower().split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

# Finds the longest word in the text
def longest_word(text):
    words = text.split()
    return max(words, key=len)

# Main function 
def analyze_text():
    try:
        # Take text input from user
        user_text = input("Enter text: ")

        # Display all results
        print("\n===== TEXT ANALYSIS =====")
        print("Words:", count_words(user_text))
        print("Vowels:", count_vowels(user_text))
        print("Consonants:", count_consonants(user_text))
        print("Reversed:", reverse_text(user_text))
        print("Palindrome:", "Yes" if is_palindrome(user_text) else "No")
        print("Without vowels:", remove_vowels(user_text))
        longest = longest_word(user_text)
        print(f"Longest word: {longest} ({len(longest)} letters)")
        print("Word Frequency:", word_frequency(user_text))

    # Handles invalid inputs
    except Exception:
        print("Invalid input.")

# calling the function
analyze_text()