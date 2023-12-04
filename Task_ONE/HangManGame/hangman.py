import random
from words import common_words

word = random.choice(common_words).upper()
guessed = []
tries = 6


def show_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]


while tries > 0:

    print(show_hangman(tries))
    guess = input("Please guess a word : ").upper()
    

    if guess == word:
        print("Congrats, you guessed the word")
        break
    
    elif guess in guessed:
        print(f"You already guessed the word {guess} and it is not the word.")

    elif len(guess) != len(word):
        print("Not a valid guess.")
        tries -= 1
        guessed.append(guess)
    
    else:
        print(f"{guess} is not the word try again.")
        guessed.append(guess)
        tries -= 1
        if tries == 0:
            print(f"Sorry you ran out of the guesses. Maybe next time. The word was {word}.")
