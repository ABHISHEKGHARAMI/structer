# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem statement : given n*n chess board and a knight is given print all the position for the chess.
print all the knights position.
'''

def isSafe(x,y,board,n):
    '''
    A utility function for check the knight position 
    is safe or not .
    '''
    if x >=0 and y >=0 and x <=n and y<=n and board[x][y] == -1:
        return True
    return False

def printSolution(n,board):
    '''
    A utility function to print 
    the solution for the knight
    '''
    for i in range(n):
        for j in range(n):
            if board[i][j] != -1:
                # print the solution
                print(board[i][j],end='\t')
                logging.info(board[i][j])
            else:
                print('.',end='\t')
                logging.info('.')
    print()
    
    
def solveKT(n,start_x,start_y):
    '''
    This utility function solve the knight problem using
    the backtracking solution using another solveKTUtil function.
    '''
    board = [[-1 for i in range(n)] for _ in range(n)]
    
    # move_x and move_y define the next move of Knight.
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # positioning the current pos
    board[start_x][start_y] = 0
    
    # positioning the knight position 
    pos = 1
    
    # check the solution exist or not 
    if not  solveKTUtil(n,board,start_x,start_y,move_x,move_y,pos):
        print('Solution does not exist')
        logging.info('Solution does not exist')
    else:
        printSolution(n,board)
        
def solveKTUtil(n,board,curr_x,curr_y,move_x,move_y,pos):
    '''
    A utility function for checking the solve knight
    '''
    if pos == n**2:
        return True
    
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        
        if isSafe(new_x,new_y,board,n):
            board[new_x][new_y] = pos
            if solveKTUtil(n,board,new_x,new_y,move_x,move_y,pos+1):
                return True
            board[new_x][new_y] = -1
            
    return False



n = int(input("enter the number of chess board block in n*n formation :"))

# get user position for knight
user_x = int(input("enter the position of x(0 to {})".format(n-1)))
user_y = int(input("enter the position of y(0 to {})".format(n-1)))

if (0<=user_x<n) and (0<=user_y<n):
    solveKT(n,user_x,user_y)
else:
    print("Invalid position for user input.")
    logging.error("Invalid position for user input.")
            
                
