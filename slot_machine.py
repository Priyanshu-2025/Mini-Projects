"""
Text-Based Slot Machine Game
----------------------------
Features:
- Start with $100 balance
- Place bets
- Spin slot machine with random symbols
- Payout system for matching symbols
"""

import random


def spin_slot_machine():
    """Return a list of 3 random symbols from slot machine."""
    symbols = ["Cherry", "Lemon", "Bell", "Diamond", "Seven"]
    return [random.choice(symbols) for _ in range(3)]


def calculate_payout(spin_result, bet):
    """Calculate winnings based on slot machine result."""
    if spin_result[0] == spin_result[1] == spin_result[2]:
        print("🎉 JACKPOT! All three match!")
        return bet * 10
    elif (spin_result[0] == spin_result[1]) or (spin_result[1] == spin_result[2]) or (spin_result[0] == spin_result[2]):
        print("✅ Two match! You win double.")
        return bet * 2
    else:
        print("😢 No match.")
        return 0


def main():
    """Main function to run the slot machine game."""
    balance = 100
    print("🎰 Welcome to the Slot Machine!")
    print(f"💰 Starting balance: ${balance}")

    while balance > 0:
        print("\n---")
        try:
            bet = int(input(f"Place your bet (1 - {balance}, or 0 to quit): "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if bet == 0:
            print("👋 Thanks for playing!")
            break
        if bet < 1 or bet > balance:
            print("❌ Invalid bet amount.")
            continue

        balance -= bet
        spin = spin_slot_machine()
        print("🎲 Spin Result:", " | ".join(spin))

        winnings = calculate_payout(spin, bet)
        balance += winnings
        print(f"💵 Current balance: ${balance}")

    if balance == 0:
        print("🪙 You're out of money. Game over!")


if __name__ == "__main__":
    main()

