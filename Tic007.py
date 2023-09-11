import numpy as np

ROWS = 3
COLUMS = 3

def mark(row,col,player):
    board[row][col] = player

def is_valid_mark(row,cal):
    return board[row][col] == 0 

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
               return False
    return True
    
board=np.zeros((ROWS,COLUMS))

game_over = False

Turn = 0

while not game_over:
     if Turn % 2 == 0:
     #Player 1
        row = int(input("Player 1: Choose row number (0-2): "))
        col = int(input("Player 1: Choose column number (0-2): "))
        if is_valid_mark(row,col):
           mark(row,col,1)
        else:
           Turn -=1
     else:
     #Player 2
        row = int(input("Player 2: Choose row number (0-2): "))
        col = int(input("Player 2: Choose column number (0-2): "))
        if is_valid_mark(row,col):
           mark(row,col,1)
        else:
           Turn -=1
          
     Turn +=1
     print(board)
     
        
     
     
