from BoardFile import *
from minimax import *
import random

running = True
player = -1
# 1 is ai -1 is human
# 1 is p2, -1 is p1

board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]
    


def random_ai(board):
    valid_cols = []

    for i in range(7):
        if board[0][i] == ".":
            valid_cols.append(i)

    col = random.choice(valid_cols)

    for i in range(5, -1, -1):
        if board[i][col] == ".":
            board[i][col] = "X" 
            break

    if check_win(board):
        display_board(board)
        print("AI wins!")
        running = False
        return

def ai_turn(board):
    valid_cols = []

    for col in range(7):
        if board[0][col] == ".":
            valid_cols.append(col)

    best_score = float("-inf")
    best_move = None

    for col in valid_cols:
        for row in range(5, -1, -1):
            if board[row][col] == ".":
                board[row][col] = "X"

                score = minimax(board, -1, 4, float("-inf"), float("inf"))

                board[row][col] = "."

                if score > best_score:
                    best_score = score
                    best_move = col

                break

    if best_move is not None:
        for row in range(5, -1, -1):
            if board[row][best_move] == ".":
                board[row][best_move] = "X"
                break


def pvp_turn(board):
    global player
    global running
    if player == 1:
        display_board(board)
        print("Player 2 turn")
        drop_piece(board, player)
        if check_win(board, player):
            display_board(board)
            print("Player 2 wins!")
            running = False
    else:
        display_board(board)
        print("Player 1 turn")
        drop_piece(board, player)
        if check_win(board, player):
            display_board(board)
            print("Player 1 wins!")
            
            running = False

    player = -player

mode = {
    1:pvp_turn,
    2:random_ai,
    3:ai_turn
}

def choose_mode():
    valid = [1,2,3]
    while True:
        try:
            print("Choose a mode")
            print("1. vs Human")
            print("2. vs random AI")
            print("3. vs Minimax AI")
            mode1 = int(input())

            if mode1 not in valid:
                print("Not a valid mode1, choose again")
            else:
                break
        except ValueError:
            print("Not a valid mode1, choose again")

    return mode1

selected = choose_mode()

while running:
    if selected == 1:
        pvp_turn(board)

    elif selected == 2 or selected == 3:
        display_board(board)
        drop_piece(board, -1)

        if check_win(board):
            display_board(board)
            print("You win!")
            running = False
            break

        if selected == 2:
            random_ai(board)
        else:
            ai_turn(board)

        if check_win(board):
            display_board(board)
            print("AI wins!")
            running = False
            break

    