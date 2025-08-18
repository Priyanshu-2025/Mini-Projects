import random

def play_ping_pong():
    player_score = 0
    computer_score = 0
    winning_score = 5

    print("Welcome to Ping Pong!")
    print("First to", winning_score, "wins.")

    while player_score < winning_score and computer_score < winning_score:
        input("Press Enter to 'hit' the ball...")
        if random.choice([True, False]):
            player_score += 1
            print("You scored a point!")
        else:
            computer_score += 1
            print("Computer scored a point!")
        print(f"Score: You {player_score} - {computer_score} Computer\n")

    if player_score == winning_score:
        print("Congratulations! You win!")
    else:
        print("Computer wins! Better luck next time.")

if __name__ == "__main__":
    play_ping_pong()
    