'''
Consider a rat placed at (0, 0) in a square matrix of order N * N. 
It has to reach the destination at (N – 1, N – 1). Find all possible paths that the rat can 
take to reach from source to destination. The directions in which the rat can move are
‘U'(up), ‘D'(down), ‘L’ (left), ‘R’ (right). Value 0 at a cell in the matrix represents 
that it is blocked and rat cannot move to it while value 1 at a cell in the matrix 
represents that rat can be travel through it. Return the list of paths in lexicographically increasing order.
'''


# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


# check for next move is it safe for the cat
def isValid(x,y,maze,visited):
    return (
        0 <= x < len(maze) and
        0 <= y < len(maze[0]) and 
        maze[x][y] == 1 and
        not visited[x][y]
    )
    
# function for solve the maze
def solveMaze(maze):
    n = len(maze)
    visited = [[False for _ in range(n)] for _ in range(n)]
    path = []
    directions = []
    
    # now go for the backtracking
    def backtracking(x,y):
        # first check x,y reach end of the maze or not
        if x == n-1 and y == n-1:
            print(f"Path found: {''.join(directions)}")
            logging.info(f"Path found: {''.join(directions)}")
            return
        
        # mark the cell as visited
        visited[x][y] = True
        
        
        # possible path and direction of the mouse
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        moves_path = ['D','R','U','L']
        
        
        for i ,(move_x,move_y) in enumerate(moves):
            new_x = x + move_x
            new_y = y + move_y
            # checking for the safety of the move
            if isValid(new_x,new_y,maze,visited):
                directions.append(moves_path[i])
                backtracking(new_x,new_y)
                directions.pop()
                
        #un-mark that path for other path
        visited[x][y] = False
        
    # call the backtrack for the starting
    backtracking(0,0)
    
    
maze = [
    [1 ,0 ,0 ,0]
    [1 ,1 ,0 ,1]
    [0 ,1 ,1 ,0]
    [1 ,1 ,1 ,1]
]

solveMaze(maze)
        
        
        