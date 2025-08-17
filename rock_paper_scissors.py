"""
Rock-Paper-Scissors vs Computer
-------------------------------
- Play best-of-N (N odd: 3, 5, 7...)
- Keeps round-by-round score
- Clear winner announcement
"""

import random
from typing import Tuple

CHOICES = ("rock", "paper", "scissors")


def read_best_of() -> int:
    while True:
        raw = input("Best of (odd number like 3/5/7): ").strip()
        if raw.isdigit():
            n = int(raw)
            if n % 2 == 1 and n > 0:
                return n
        print("❌ Please enter a positive odd number.")


def get_user_choice() -> str:
    while True:
        c = input("Choose (rock/paper/scissors): ").strip().lower()
        if c in CHOICES:
            return c
        print("❌ Invalid choice.")


def decide_round(user: str, comp: str) -> Tuple[int, int]:
    if user == comp:
        print("⚖️  Tie.")
        return 0, 0
    wins = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    if (user, comp) in wins:
        print("✅ You win this round!")
        return 1, 0
    print("❌ Computer wins this round.")
    return 0, 1


def main():
    print("✊✋✌️ Rock-Paper-Scissors")
    total = read_best_of()
    to_win = total // 2 + 1

    user_score = 0
    comp_score = 0

    round_no = 1
    while user_score < to_win and comp_score < to_win:
        print(f"\n--- Round {round_no} ---")
        user = get_user_choice()
        comp = random.choice(CHOICES)
        print(f"🧑 You: {user}  |  🤖 Computer: {comp}")
        u, c = decide_round(user, comp)
        user_score += u
        comp_score += c
        print(f"Score → You {user_score} : {comp_score} Computer")
        round_no += 1

    if user_score > comp_score:
        print("\n🏆 You win the match!")
    else:
        print("\n🤖 Computer wins the match!")
    print("👋 Thanks for playing!")


if __name__ == "__main__":
    main()