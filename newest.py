from IPython.display import clear_output
import random
player1 = input("Enter name of Player 1!")
player2 = input("Enter name of Player 2!")
symb1 = ""
symb2 = ""
board = ["","","","","","","","",""]

def display_board(board):
    print(board[0]+" | "+board[1]+" | "+board[2] + "\n---------" )
    print(board[3]+" | "+board[4]+" | "+board[5] + "\n---------")
    print(board[6]+" | "+board[7]+" | "+board[8])

def choose_player():
    b = random.randint(1,2)
    if b == 1:
        return(player1)
    if b ==2:
        return(player2)

def player_input():
    choice = input(choose_player()+ " choose X or O!")
    if choice not in ["X", "O"]:
        print("Error. Please only choose X or O")
    elif choice == "X":
        return("X")
    else:
        return("O")

player_input()

def winorno():
    if board[0] == board [1] == board[3]:    
        return True
    if board 
