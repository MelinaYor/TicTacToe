import random #Used Random lib for the bot


board = ["-","-","-","-","-","-","-","-","-",]

currentPlayer= "X"
winner = None
gameRunning = True



#GameBoard
def pBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#Take PlayerInput

def pInput(board):
    inp = int(input("Enter a number between 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else: 
        print("Spot already used")


def CheckHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True 
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[3]
        return True 
    
    
def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    

def checkTie(board):
    global gameRunning
    if "-" not in board:
        pBoard(board)
        print("Tie")
        gameRunning = False
        
def checkWinner():
    global gameRunning
    if checkDiag(board) or CheckHorizontal(board) or checkRow(board): 
        print(f"The Winner is {winner}")
       
#SwitchPlayers

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
        
        
#botplayer

def bot(board):
    while currentPlayer == "O":
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = "O"
            switchPlayer()
    
while gameRunning:
    pBoard(board)
    pInput(board)
    checkWinner()
    checkTie(board)
    switchPlayer()
    bot(board) 
    checkWinner()
    checkTie(board)