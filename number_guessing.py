"""
Number Guessing Game
--------------------
- Difficulty levels: Easy(1-20), Medium(1-50), Hard(1-100)
- Tracks attempts; stores best score per difficulty in a local JSON file.
"""

import json
import os
import random
from typing import Dict

SCORES_FILE = "guess_highscores.json"


def load_scores() -> Dict[str, int]:
    if not os.path.exists(SCORES_FILE):
        return {}
    try:
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_scores(scores: Dict[str, int]) -> None:
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)


def choose_difficulty() -> str:
    print("\nChoose difficulty:")
    print("1) Easy   (1-20)")
    print("2) Medium (1-50)")
    print("3) Hard   (1-100)")
    mapping = {"1": "easy", "2": "medium", "3": "hard"}
    while True:
        c = input("Enter 1/2/3: ").strip()
        if c in mapping:
            return mapping[c]
        print("❌ Invalid choice.")


def get_range(level: str) -> int:
    return {"easy": 20, "medium": 50, "hard": 100}[level]


def play_once(level: str) -> int:
    upper = get_range(level)
    secret = random.randint(1, upper)
    attempts = 0
    print(f"\n🎯 I picked a number between 1 and {upper}. Try to guess it!")

    while True:
        guess_str = input("Your guess: ").strip()
        if not guess_str.isdigit():
            print("❌ Enter a valid positive integer.")
            continue
        guess = int(guess_str)
        attempts += 1

        if guess < secret:
            print("📉 Too low.")
        elif guess > secret:
            print("📈 Too high.")
        else:
            print(f"🎉 Correct! You got it in {attempts} attempts.")
            return attempts


def main():
    print("🎲 Number Guessing Game")
    scores = load_scores()

    while True:
        level = choose_difficulty()
        best = scores.get(level)
        if best:
            print(f"🏆 Best ({level}): {best} attempts")

        attempts = play_once(level)
        if best is None or attempts < best:
            scores[level] = attempts
            save_scores(scores)
            print("✨ New high score!")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()