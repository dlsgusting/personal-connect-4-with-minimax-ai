from BoardFile import *
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
    ["X", ".", ".", ".", ".", ".", "."],
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
            return

def ai_turn(board):
    best_score = -999
    best_move = None

    for pos in range(len(board)):
        if board[pos] == "?":
            board[pos] = "X"
            score = minimax(board, -1)
            board[pos] = "?"
            
            if score > best_score:
                best_score = score
                best_move = pos

    if best_move is not None:
        board[best_move] = "X"

    for i in range(5,-1,-1):
        for i in range(7)
            if board[i][col] == ".":
                if player == 1:
                    board[i][col] = "X"
                    break
                else:
                    board[i][col] = "O"
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
    1:pvp_turn
}

def choose_mode():
    valid = [1]
    while True:
        try:
            print("Choose a mode")
            print("1. vs Human")
            print("2. vs random AI")
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

    mode[selected](board)



    