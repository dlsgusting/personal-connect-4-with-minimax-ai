board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    ["X", ".", ".", ".", ".", ".", "."],
]

def display_board(board):
    print("\n           CONNECT FOUR\n")
    print("    1   2   3   4   5   6   7")

    top =    "  ┌───┬───┬───┬───┬───┬───┬───┐"
    middle = "  ├───┼───┼───┼───┼───┼───┼───┤"
    bottom = "  └───┴───┴───┴───┴───┴───┴───┘"

    print(top)

    row_num = 6
    for row in board:
        print(f"{row_num} │ " + " │ ".join(row) + " │")

        if row_num != 1:
            print(middle)

        row_num -= 1

    print(bottom)

def drop_piece(board, player):
    valid = [1,2,3,4,5,6,7]
    while True:
        try:
            print("Choose a column 1-7")
            col = int(input())

            if col not in valid or board[0][col-1] == "X" or board[0][col-1] == "O":
                print("Column full or invalid column")
            else:
                break
        except ValueError:
            print("Not a valid column, choose again")

    col -=1

    for i in range(5,-1,-1):
        if board[i][col] == ".":
            if player == 1:
                board[i][col] = "X"
                break
            else:
                board[i][col] = "O"
                break