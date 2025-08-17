"""
Tic-Tac-Toe (CLI)
-----------------
Modes:
- Player vs Player
- Player vs Computer (unbeatable AI using minimax)
"""

from typing import List, Optional, Tuple

EMPTY = " "
HUMAN = "X"
AI = "O"
WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]


def print_board(b: List[str]) -> None:
    print("\n")
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print("\n")


def winner(b: List[str]) -> Optional[str]:
    for a, c, d in WIN_COMBOS:
        if b[a] == b[c] == b[d] != EMPTY:
            return b[a]
    if EMPTY not in b:
        return "draw"
    return None


def available_moves(b: List[str]) -> List[int]:
    return [i for i, v in enumerate(b) if v == EMPTY]


def minimax(b: List[str], is_ai_turn: bool) -> Tuple[int, Optional[int]]:
    """
    Returns (score, move)
    score: +1 (AI win), -1 (Human win), 0 (draw)
    """
    w = winner(b)
    if w == AI:
        return (1, None)
    if w == HUMAN:
        return (-1, None)
    if w == "draw":
        return (0, None)

    best_move = None
    if is_ai_turn:
        best_score = -2
        for m in available_moves(b):
            b[m] = AI
            score, _ = minimax(b, False)
            b[m] = EMPTY
            if score > best_score:
                best_score, best_move = score, m
        return best_score, best_move
    else:
        best_score = 2
        for m in available_moves(b):
            b[m] = HUMAN
            score, _ = minimax(b, True)
            b[m] = EMPTY
            if score < best_score:
                best_score, best_move = score, m
        return best_score, best_move


def read_move(b: List[str]) -> int:
    while True:
        s = input("Enter position (1-9): ").strip()
        if s.isdigit():
            pos = int(s) - 1
            if 0 <= pos <= 8 and b[pos] == EMPTY:
                return pos
        print("❌ Invalid move. Choose an empty cell 1-9.")


def play_pvp():
    b = [EMPTY] * 9
    current = HUMAN  # X always first
    print("🎮 Tic-Tac-Toe (Player vs Player)")
    while True:
        print_board(b)
        print(f"Turn: {current}")
        pos = read_move(b)
        b[pos] = current
        w = winner(b)
        if w:
            print_board(b)
            if w == "draw":
                print("🤝 It's a draw!")
            else:
                print(f"🏆 {w} wins!")
            return
        current = AI if current == HUMAN else HUMAN


def play_vs_ai():
    b = [EMPTY] * 9
    print("🤖 Tic-Tac-Toe (You vs Computer)")
    human_first = input("Do you want to go first? (y/n): ").strip().lower() == "y"
    while True:
        print_board(b)
        if human_first:
            # human turn
            print("Your turn (X)")
            pos = read_move(b)
            b[pos] = HUMAN
            w = winner(b)
            if w:
                print_board(b)
                if w == "draw":
                    print("🤝 It's a draw!")
                else:
                    print("🏆 You win!")
                return
            # AI turn
            _, m = minimax(b, True)
            b[m] = AI
            w = winner(b)
            if w:
                print_board(b)
                if w == "draw":
                    print("🤝 It's a draw!")
                else:
                    print("🤖 Computer wins!")
                return
        else:
            # AI turn first
            print("Computer's turn (O)")
            _, m = minimax(b, True)
            b[m] = AI
            w = winner(b)
            if w:
                print_board(b)
                if w == "draw":
                    print("🤝 It's a draw!")
                else:
                    print("🤖 Computer wins!")
                return
            # Human turn
            print_board(b)
            print("Your turn (X)")
            pos = read_move(b)
            b[pos] = HUMAN
            w = winner(b)
            if w:
                print_board(b)
                if w == "draw":
                    print("🤝 It's a draw!")
                else:
                    print("🏆 You win!")
                return


def main():
    print("Tic-Tac-Toe")
    print("1) Player vs Player")
    print("2) Player vs Computer (Unbeatable)")
    while True:
        c = input("Choose mode (1/2): ").strip()
        if c == "1":
            play_pvp()
            break
        elif c == "2":
            play_vs_ai()
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
