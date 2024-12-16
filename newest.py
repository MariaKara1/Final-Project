from IPython.display import clear_output

def display_board(board):
    print(board[0]+" | "+board[1]+" | "+board[2] + "\n---------" )
    print(board[3]+" | "+board[4]+" | "+board[5] + "\n---------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def player_input():
    choice = input(player1 + " choose X or O!")
    if choice not in ["X", "O"]:
        print("Error. Please only choose X or O")
    elif choice == "X":
        return("X","O")
    else:
        return("O","X")

def place_marker(board, marker, position):
    board[position] = marker

