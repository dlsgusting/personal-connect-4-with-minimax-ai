running = True

board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

def display_board(board):
    print("\n           CONNECT FOUR\n")
    print("    1   2   3   4   5   6   7")

    top = "  ┌───┬───┬───┬───┬───┬───┬───┐"
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

while running:
    display_board(board)
    break