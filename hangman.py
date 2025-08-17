"""
Hangman Game in Python
----------------------
Classic word guessing game:
- Player has 6 attempts
- Guess letters one by one
- Win if the full word is revealed
"""

import random


def get_random_word():
    """Return a random word from the word list."""
    word_list = ["python", "hangman", "programming", "challenge", "developer"]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Return word display with guessed letters revealed."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    """Main function for Hangman game."""
    print("🎮 Welcome to Hangman!")

    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\n🎉 Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts}")

    else:
        print(f"\n💀 Game over! The word was: {word}")


if __name__ == "__main__":
    hangman()
