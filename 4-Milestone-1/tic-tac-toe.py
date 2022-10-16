row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

board = [row1, row2, row3]

color = {"message": "\033[90m", "error": "\033[91m", "Player1": "\033[94m", "Player2" : "\033[95m", "bold": "\033[1m", "end": "\033[0m"}

def reset_board():
    for index,x in enumerate(board):
        for innerIndex,y in enumerate(x):
            board[index][innerIndex] = ' '

def text_color(symbol): 
    return (color['Player2'] + symbol + color['end'],color['Player1'] + symbol + color['end'])[symbol == 'X']

def display_board(): 
    print('-------------')
    print('|   |   |   |')
    print('| ' + text_color(board[0][0]) + ' | ' + text_color(board[0][1]) + ' | ' + text_color(board[0][2]) + ' | ')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| ' + text_color(board[1][0]) + ' | ' + text_color(board[1][1]) + ' | ' + text_color(board[1][2]) + ' | ')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| ' + text_color(board[2][0]) + ' | ' + text_color(board[2][1]) + ' | ' + text_color(board[2][2]) + ' | ')
    print('|   |   |   |')
    print('-------------')

def get_position(type, player):
    position = "WRONG"
    within_range = False
    empty_row = False
    input_msg = f"{color[player]}Select your {type}: [1, 2, 3] {color['end']}"

    while position.isdigit() == False or within_range == False or empty_row == False:
        position = input(input_msg)

        if position.isdigit() == False:
            print(f"{color['error']}Sorry, please enter a valid {type} : [1, 2, 3] {color['end']}")
        
        if position.isdigit() == True:
            if int(position) not in [1, 2, 3]:
                print(f"{color['error']}Please choose the {type} between 1 and 3 {color['end']}")
                within_range = False
            else:
                within_range = True
                if type == "row" and ' ' not in board[int(position) - 1]:
                    print(f"{color['error']}No empty field in the selected {type}. Try again.. {color['end']}")
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
    
def validate_selection(row, index, player):
    invalid_index = False

    if board[row - 1][index - 1] != ' ':
        invalid_index = True

    while invalid_index == True:
        print(f"{color['error']}You can't choose this position. Try different position. {color['end']}")
        index = get_position("position", player)
        if board[row - 1][index - 1] != ' ':
            invalid_index = True
        else:
            invalid_index = False
    return row, index

def verify_move(player, symbol):
    if check_for_win(symbol) == True:
        print(f"{color['bold']}{color['message']}Congratulations!!! {player[symbol]} won the game!!! {color['end']}")
        return True
    elif (' ' not in row1) and (' ' not in row2) and (' ' not in row3) :
        print(f"{color['bold']}{color['message']}Match ended in Draw!!! {color['end']}")            
        return True
    else:
        return False

def get_user_input():
    player = {"X": "Player1", "Y": 'Player2'}
    match_ended = False
    count = 0
    symbol = "X"

    while match_ended == False:
        if count%2 == 0: symbol = "X"; print(f"{color['Player1']}{player[symbol]}'s Turn:{color['end']}")
        else: symbol = "Y"; print(f"{color['Player2']}{player[symbol]}'s Turn:{color['end']}")

        row_val = get_position("row", player[symbol])
        index_val = get_position("index", player[symbol])
        row, index = validate_selection(row_val, index_val, player[symbol])

        board[row - 1 ][index - 1] = symbol
        display_board()
        match_ended = verify_move(player, symbol)
        count += 1

def play():
    print(f"{color['bold']}{color['message']}Welcome to the game: Tic Tac Toe!!! {color['end']}")
    play_game = "WRONG"

    while play_game not in ['Y', 'N', 'y', 'n']:
        play_game = input(f"{color['message']}Would you like to start a new game?: ['Y', 'N'] {color['end']}")

        if play_game not in ['Y', 'N', 'y', 'n']:
            print(f"{color['error']}Invalid input. Try again... Choose either Y or N{color['end']}")

        if play_game in ["Y", "y"]:
            display_board()
            get_user_input()
            reset_board()
            play_game = "WRONG"
        elif play_game in ["N", "n"]:
            print(f"{color['message']}Bye.. See you here soon!!!{color['end']}")

play()