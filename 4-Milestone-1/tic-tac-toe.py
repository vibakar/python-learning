row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

board = [row1, row2, row3]

color = {"blue": "\033[94m", "pink": "\033[90m", "red": "\033[91m", "end": "\033[0m"}

def reset_board():
    for index,x in enumerate(board):
        for innerIndex,y in enumerate(x):
            board[index][innerIndex] = ' '

def display_board(rows): 
    print('-------------')
    print('|   |   |   |')
    print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' | ')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' | ')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' | ')
    print('|   |   |   |')
    print('-------------')

def get_position(arg):
    position = "WRONG"
    within_range = False
    empty_row = False
    input_msg = f"{color['blue']}Select your {arg}: [1, 2, 3] {color['end']}"

    while position.isdigit() == False or within_range == False or empty_row == False:
        position = input(input_msg)

        if position.isdigit() == False:
            print(f"{color['red']}Sorry, please enter a valid {arg} : [1, 2, 3] {color['end']}")
        
        if position.isdigit() == True:
            if int(position) not in [1, 2, 3]:
                print(f"{color['red']}Please choose the {arg} between 1 and 3 {color['end']}")
                within_range = False
            else:
                within_range = True
                if arg == "row" and ' ' not in board[int(position) - 1]:
                    print(f"{color['red']}No empty field in the selected {arg}. Try again.. {color['end']}")
                    empty_row = False
                else:
                    empty_row = True
    return int(position)

def check_for_win(symbol):
    if len(list(set(row1))) == 1 and row1[0] == symbol:
        return True
    elif len(list(set(row2))) == 1 and row2[0] == symbol:
        return True
    elif len(list(set(row3))) == 1 and row3[0] == symbol:
        return True
    elif row1[0] == symbol and row2[0] == symbol and row3[0] == symbol:
        return True
    elif row1[1] == symbol and row2[1] == symbol and row3[1] == symbol:
        return True
    elif row1[2] == symbol and row2[2] == symbol and row3[2] == symbol:
        return True
    elif row1[0] == symbol and row2[1] == symbol and row3[2] == symbol:
        return True
    elif row1[2] == symbol and row2[1] == symbol and row3[0] == symbol:
        return True
    else:
        return False
    
def validate_selection(row, index):
    invalid_index = False

    if board[row - 1][index - 1] != ' ':
        invalid_index = True

    while invalid_index == True:
        print(f"{color['red']}You can't choose this position. Try different position. {color['end']}")
        index = get_position("position")
        if board[row - 1][index - 1] != ' ':
            invalid_index = True
        else:
            invalid_index = False
    return row, index

def verify_move(player, symbol):
    if check_for_win(symbol) == True:
        print(f"{color['pink']}{player[symbol]} won the game!!! {color['end']}")
        return True
    elif (' ' not in row1) and (' ' not in row2) and (' ' not in row3) :
        print(f"{color['pink']}Match ended in Draw!!! {color['end']}")            
        return True
    else:
        return False

def get_user_input():
    player = {"X": "Player1", "Y": 'Player2'}
    match_ended = False
    count = 0
    symbol = "X"

    while match_ended == False:
        if count%2 == 0: symbol = "X"; print(f"{color['blue']}{player[symbol]}'s Turn:{color['end']}")
        else: symbol = "Y"; print(f"{color['blue']}{player[symbol]}'s Turn:{color['end']}")

        row_val = get_position("row")
        index_val = get_position("index")
        row, index = validate_selection(row_val, index_val)

        board[row - 1 ][index - 1] = symbol
        display_board(board)
        match_ended = verify_move(player, symbol)
        count += 1

def play():
    print(f"{color['blue']}Welcome to game: Tic Tac Toe!!! {color['end']}")
    play_game = "WRONG"

    while play_game not in ['Y', 'N', 'y', 'n']:
        play_game = input(f"{color['blue']}Would you like to start a new game?: ['Y', 'N'] {color['end']}")

        if play_game not in ['Y', 'N', 'y', 'n']:
            print(f"{color['red']}Invalid input. Try again... Choose either Y or N{color['end']}")

        if play_game in ["Y", "y"]:
            display_board(board)
            get_user_input()
            reset_board()
            play_game = "WRONG"
        elif play_game in ["N", "n"]:
            print(f"{color['blue']}Bye.. See you here soon!!!{color['end']}")

play()