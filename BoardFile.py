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

def hori(board, row, col):
    if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
        return True
    else:
        return False

def vert(board, row, col):
    if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] :
        return True
    else:
        return False

def diag1(board, row, col):
    if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
        return True
    else:
        return False

def diag2(board, row, col):
    if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
        return True
    else:
        return False

def check_win(board):
    for row in range(0,6):
        for col in range(0,7):
            if board[row][col] == ".":
                continue
            else:
                if col <= 3:
                    if hori(board, row, col):
                        return True
                if row <= 2:
                    if vert(board, row, col):
                        return True
                if row <= 2 and col <= 3:
                    if diag1(board, row, col):
                        return True
                if row>= 3 and col <= 3:
                    if diag2(board, row, col):
                        return True
    return False


                

