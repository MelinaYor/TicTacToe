import random #Used Random lib for the bot
import threading

board = ["-","-","-","-","-","-","-","-","-",]

currentPlayer = input("Do you want to start with X or O? ").upper()
while currentPlayer not in ["X", "O"]:
    currentPlayer = input("Invalid input. Please enter either X or O: ").upper()

if currentPlayer == "X":
    botPlayer = "O"
else:
    botPlayer = "X"

winner = None
gameRunning = True
timeIsUp = False


#GameBoard
def pBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#Take PlayerInput

def pInput(board):
    inp = input("Enter a number between 1-9:")
    while not inp.isdigit() or int(inp) < 1 or int(inp) > 9:
        inp = input("Invalid input. Please enter a number between 1-9: ")
    inp = int(inp)
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
        return True
    else:
        print("Spot already used")
        return False

def CheckHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-" and board[0] == currentPlayer:
        winner = currentPlayer
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-" and board[3] == currentPlayer:
        winner = currentPlayer
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-" and board[6] == currentPlayer:
        winner = currentPlayer
        return True 

    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-" and board[0] == currentPlayer:
        winner = currentPlayer
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-" and board[1] == currentPlayer:
        winner = currentPlayer
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-" and board[2] == currentPlayer:
        winner = currentPlayer
        return True 
        
def checkDiag(board):
    global winner 
    if (board[0]==board [4]==board [8]) and (board [0]!= "-") and (board [0]==currentPlayer):
        winner=currentPlayer
        return True
    if (board [2]==board [4]==board [6]) and (board [2]!= "-") and (board [2]==currentPlayer):
        winner=currentPlayer
        return True
    

def checkTie(board):
    global gameRunning
    if "-" not in board:
        pBoard(board)
        print("Tie")
        gameRunning = False
    
def checkWinner():
    global gameRunning
    if CheckHorizontal(board) or checkRow(board) or checkDiag(board):
        pBoard(board)
        print(winner + " has won the game ")
        gameRunning = False    

        
#SwitchPlayers

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
        
        
#botplayer

def bot(board):
    while currentPlayer == botPlayer:
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = botPlayer
            switchPlayer()
    
while gameRunning:
    pBoard(board)
    if pInput(board):
        checkWinner()
        checkTie(board)
        switchPlayer()
        if gameRunning:
            bot(board)
            checkWinner()
            checkTie(board)


