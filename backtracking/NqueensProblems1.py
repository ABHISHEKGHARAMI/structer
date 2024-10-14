# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()

'''
Problem statement :
The eight queens problem is the problem of placing eight queens on an 8×8 chessboard 
such that none of them attack one another (no two are in the same row, column, or diagonal. 
'''
N = 8

def solveNqueens(board,col):
    if col == N:
        print("\n".join(
            [" ".join(["Q" if col == 1 else "." for col in row]) for row in board]))
        logging.info(board)
        return True
    
    # else
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col] = 1
            if solveNqueens(board,col+1):
                return True
            board[i][col] = 0
    return False
    
    
# checking for the safe space for the queen
def isSafe(board,row,col):
    # first : check the game is started
    for i in range(N):
        if board[row][i]== 1:
            return False
        
    # second the upper diagonal for the chess
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y] == 1:
            return False
        
    # third check the lower diagonal
    for x,y in zip(range(row,N,1),range(col,-1,-1)):
        if board[x][y] == 1:
            return False
        
    return True


# checking the solution
board = [[0 for x in range(N)] for y in range(N)]
if not solveNqueens(board,0):
    print("No solution exist.")
    logging.info("No solution exist.")