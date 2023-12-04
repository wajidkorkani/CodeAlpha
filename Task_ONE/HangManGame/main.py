import random
from words import all_words_list

def get_word():
    return random.choice(all_words_list).upper()

def display_hangman(tries):
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

def play(word):
    word_completion = "_" * len(word)
    guessed_letters, guessed_words = set(), set()
    tries = 6

    print("Let's play Hangman!\n")

    while tries > 0:
        print(display_hangman(tries))
        print(word_completion)

        guess = input("Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.add(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.add(guess)
                word_completion = ''.join([c if letter == guess else c for c, letter in zip(word_completion, word)])
                if "_" not in word_completion:
                    print("Congrats, you guessed the word! You win!")
                    return
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.add(guess)
            else:
                print("Congrats, You win!")
                return
        else:
            print("Not a valid guess.")

    print(display_hangman(tries))
    print(f"Sorry, you ran out of tries. The word was {word}. GoodLuck for next time!")

def main():
    while True:
        word = get_word()
        play(word)
        if input("Do you want to play Again? (Y/N) ").upper() != "Y":
            break

if __name__ == "__main__":
    main()
