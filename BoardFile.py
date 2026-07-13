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

            if col not in valid or board[0][col-1] != ".":
                print("Column full or invalid")
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

def check_win(board):
    rows = 6
    cols = 7

    # Horizontal
    for row in range(rows):
        for col in range(cols - 3):
            piece = board[row][col]

            if piece != "." and all(board[row][col + i] == piece for i in range(4)):
                return piece

    # Vertical
    for row in range(rows - 3):
        for col in range(cols):
            piece = board[row][col]

            if piece != "." and all(board[row + i][col] == piece for i in range(4)):
                return piece

    # Diagonal down right
    for row in range(rows - 3):
        for col in range(cols - 3):
            piece = board[row][col]

            if piece != "." and all(board[row + i][col + i] == piece for i in range(4)):
                return piece

    # Diagonal up right
    for row in range(3, rows):
        for col in range(cols - 3):
            piece = board[row][col]

            if piece != "." and all(board[row - i][col + i] == piece for i in range(4)):
                return piece

    return False


                

