# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem statement : You have supplied to the m * n grids to go , find the number of the moves where 
you can go from start to end using the dynamic tabular approach.
'''

def grid_dynamics(m,n):
    grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    #base case
    grid[1][1] = 1
    
    for i in range(m+1):
        for j in range(n+1):
            current = grid[i][j]
            
            if i+1<=m:
                current += grid[i+1][j]
            if j + 1 <= n :
                current += grid[i][j+1]
                
    return grid[m][n]

print(f"the step require for the grid is : {grid_dynamics(3,4)}")
logging.info(f"the step require for the grid is : {grid_dynamics(3,4)}")
