import random

BOARD_POSITION = [['11','12','13'],['21','22','23'],['31','32','33']]

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def print_position():
    for row in BOARD_POSITION:
        print(" ".join(map(str, row)))

def check_status(filled):
    win = False
    row=[]
    col=[]
    for cell in filled:
        row.append(int(cell[0]))
        col.append(int(cell[1]))

    for i in range(1,4):
        if row.count(i) >= 3:
            win = True
            break
        if col.count(i) >= 3:
            win = True
            break
    if win == False:
        if '11' in filled and '22' in filled and '33' in filled:
            win = True
        if '13' in filled and '22' in filled and '31' in filled:
            win = True
    return win

def is_board_filled(full_list):
    if len(full_list) == 0:
        return True
    else:
        return False

def update_board(position, player, board):
    row=int(position[0])-1
    col=int(position[1])-1
    board[row][col]=player
    return board


def play_game(board):
    winner =""
    print_position()
    is_game_over = False
    full_list = ['11','12','13','21','22','23','31','32','33']
    my_pos = []
    opponent_pos = []
    while not is_game_over:        
        position = input("Player A: Enter position number: ")
        my_pos.append(position)
        full_list.remove(position)

        if is_board_filled(full_list):
            is_game_over = True
            break

        board = update_board(position, 'X', board)
        print_board(board)
        print(f"my postions : {my_pos}")
        if (len(my_pos) > 2):
            if check_status(my_pos):
                is_game_over = True
                winner = "Player A"
                break

        opponent_position = input("Player B: Enter position number: ")
        full_list.remove(opponent_position)
        if is_board_filled(full_list):
            is_game_over = True
            break

        opponent_pos.append(opponent_position)
        board = update_board(opponent_position, 'O', board)       
        print_board(board)

        print(f"opponent postions : {opponent_pos}")
        if (len(opponent_pos) > 2):
            if check_status(opponent_pos):
                is_game_over = True
                winner = "Player B"
                break

    if is_game_over and winner == "":
        print("Match Draw")
    else:
        print (f"{winner} won.")

while input("Do you want to play Tic Tac Toe? Type 'y' or 'n': ") == "y":
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    play_game(board)