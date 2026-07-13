from BoardFile import *

def evaluate_window(window):
    score = 0

    # X scores
    if window.count("X") == 4:
        score += 100000

    elif window.count("X") == 3 and window.count(".") == 1:
        score += 100

    elif window.count("X") == 2 and window.count(".") == 2:
        score += 10

    elif window.count("X") == 1 and window.count(".") == 3:
        score += 1


    # O scores
    if window.count("O") == 4:
        score -= 100000

    elif window.count("O") == 3 and window.count(".") == 1:
        score -= 120

    elif window.count("O") == 2 and window.count(".") == 2:
        score -= 10

    elif window.count("O") == 1 and window.count(".") == 3:
        score -= 1

    return score
    

def score_position(board):
    rows = 6
    cols = 7

    score = 0

    # Horizontal
    for row in range(rows):
        for col in range(cols - 3):
            hori = [
                board[row][col],
                board[row][col + 1],
                board[row][col + 2],
                board[row][col + 3]
            ]
            score += evaluate_window(hori)

    # Vertical
    for row in range(rows - 3):
        for col in range(cols):
            vert = [
                board[row][col],
                board[row + 1][col],
                board[row + 2][col],
                board[row + 3][col]
            ]
            score += evaluate_window(vert)

    # Diagonal down right
    for row in range(rows - 3):
        for col in range(cols - 3):
            diag1 = [
                board[row][col],
                board[row + 1][col + 1],
                board[row + 2][col + 2],
                board[row + 3][col + 3]
            ]
            score += evaluate_window(diag1)

    # Diagonal up right
    for row in range(3, rows):
        for col in range(cols - 3):
            diag2 = [
                board[row][col],
                board[row - 1][col + 1],
                board[row - 2][col + 2],
                board[row - 3][col + 3]
            ]
            score += evaluate_window(diag2)

    return score

def minimax(board, current_turn, depth):
    result = check_win(board)

    if result == "X":
        return 1000000
    elif result == "O":
        return -1000000

    if depth == 0:
        return score_position(board)

    valid_cols = []

    for col in range(7):
        if board[0][col] == ".":
            valid_cols.append(col)

    if not valid_cols:
        return 0

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


