from BoardFile import *
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

def pvp_turn(board):
    global player
    if player == 1:
        display_board(board)
        print("Player 2 turn")
        drop_piece(board, player)
        if check_win(board, player):
            display_board(board)
            print("Player 2 wins")
            global running
            running = False
    else:
        display_board(board)
        print("Player 1 turn")
        drop_piece(board, player)
        if check_win(board, player):
            display_board(board)
            print("Player 1 wins")
            global running
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
            print("1/vs Human, 2/vs AI")
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



    