from BoardFile import *

def evaluate_window(window, ai_piece, player_piece):
    return
    

def score_position(board):
    rows = 6
    cols = 7

    score = 0

    # Horizontal
    hori = []
    for row in range(rows):
        for col in range(cols - 3):
            hori.append(board[row][col])
            score += evaluate_window(hori, "X", "O")
            hori = []

    # Vertical
    vert = []
    for row in range(rows - 3):
        for col in range(cols):
            vert.append(board[row][col])

    # Diagonal down right
    diag1 = []
    for row in range(rows - 3):
        for col in range(cols - 3):
            diag1.append(board[row][col])

    # Diagonal up right
    diag2 = []
    for row in range(3, rows):
        for col in range(cols - 3):
            diag2.append(board[row][col])

def minimax(board, current_turn, depth):
    result = check_win(board)

    if result == "ai":
        return 1
    elif result == "player":
        return -1
    elif result == 0:
        return 0

    if depth == 0:
        return 0

    valid_cols = []

    for col in range(7):
        if board[0][col] == ".":
            valid_cols.append(col)

    if current_turn == 1:
        best_score = float("-inf")

        for col in valid_cols:
            for row in range(5, -1, -1):
                if board[row][col] == ".":
                    board[row][col] = "X"

                    score = minimax(board, -1, depth - 1)
                    best_score = max(score, best_score)

                    board[row][col] = "."
                    break

        return best_score

    else:
        best_score = float("inf")

        for col in valid_cols:
            for row in range(5, -1, -1):
                if board[row][col] == ".":
                    board[row][col] = "O"

                    score = minimax(board, 1, depth - 1)
                    best_score = min(score, best_score)

                    board[row][col] = "."
                    break

        return best_score


