from IPython.display import clear_output
import random
player1 = input("Enter name of Player 1!")
player2 = input("Enter name of Player 2!")
symb = ["",""]
board = ["0","1","2","3","4","5","6","7","8"]
choice = input(player1+ " choose X or O!")

def display_board(board):
    print(board[0]+" | "+board[1]+" | "+board[2] + "\n---------" )
    print(board[3]+" | "+board[4]+" | "+board[5] + "\n---------")
    print(board[6]+" | "+board[7]+" | "+board[8])




def player_input():
    if choice not in ["X", "O"]:
        print("Error. Please only choose X or O")
    elif choice == "X":
        return("X")
    else:
        return("O")

def which_one():
    if player_input() == "X":
        symb[0] = "X"
        symb[1]= "O"
    else:
        symb[0] = "O"
        symb[1]= "X"

which_one()

player_input()

def winorno():
    if board[0] == board [1] == board[3] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:    
        return True
    if board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    else:
        return False

def playing():
    players = [player1, player2, player1, player2, player1, player2, player1, player2, player1]
    i=0
    while winorno() == False:
       
        b = int(input(players[i] + ", what position would you like to play? Choose from 0-8"))
        if i%2 == 0:
            board[b] = symb[0]
        else:
            board[b] = symb[1]
        i+=1
        display_board(board)
        if i == 8:
            break
            return False

playing()
        
def ending():
    if winorno() == True:
        if board[0] == board [1] == board[3] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:   