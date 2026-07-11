from BoardFile import *

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