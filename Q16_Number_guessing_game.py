

import random

# Main function 
def guessing_game():
    # choose a random number
    secret_number = random.randint(1, 100)

   
    attempts = 7

    
    for i in range(attempts):
        try:
            # inlut from user
            guess = int(input("Enter guess: "))

            
            if guess == secret_number:
                print("Correct! You guessed it.")
                return
            elif guess < secret_number:
                print("Too low.")
            else:
                print("Too high.")

            # Show remaining attempts after each wrong guess
            print("Attempts left:", attempts - i - 1)

        # Handles invalids
        except:
            print("Invalid input.")

    
    print("Game Over! Number was:", secret_number)

# calling the function
guessing_game()