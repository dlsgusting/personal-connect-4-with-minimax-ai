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

            if col not in valid:
                print("Not a valid column, choose again")
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

def pvp_turn(board):
    global player
    if player == 1:
        display_board(board)
        print("Player 2 turn")
        drop_piece(board, player)
    else:
        display_board(board)
        print("Player 1 turn")
        drop_piece(board, player)

    player = -player

mode = {
    1:pvp_turn
}

def choose_mode():
    while True:
        try:
            print("Choose a mode")
            print("1/vs Human, 2/vs AI")
            mode1 = int(input())

            if mode1 not in mode:
                print("Not a valid mode1, choose again")
            else:
                break
        except ValueError:
            print("Not a valid mode1, choose again")

    return mode1

selected = choose_mode()

while running:
    mode[selected](board)



    