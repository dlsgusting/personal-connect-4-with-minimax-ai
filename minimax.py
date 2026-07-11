from BoardFile import *

def minimax(board, current_turn):
    result = check_win(board, current_turn)

    if result == "ai":
        return 1
    elif result == "player":
        return -1
    elif result == 0:
        return 0

    if current_turn == 1:
        valid_cols = []

        for col in range(7):
            if board[0][col] == ".":
                valid_cols.append(col)

        best_score = float("-inf")

        for col in valid_cols:
            for row in range(5, -1, -1):
                if board[row][col] == ".":
                    board[row][col] = "X"

                    score = minimax(board, -1)
                    best_score = min(score, best_score)

                    board[row][col] = "."

        return best_score

    else:
        valid_cols = []

        for col in range(7):
            if board[0][col] == ".":
                valid_cols.append(col)

        best_score = float("-inf")

        for col in valid_cols:
            for row in range(5, -1, -1):
                if board[row][col] == ".":
                    board[row][col] = "X"

                    score = minimax(board, 1)
                    best_score = min(score, best_score)

                    board[row][col] = "."


        return best_score
