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
    grid = [[0]*n for _ in range(m)]
    grid[0][0] = 0
    grid[1][1] = 1
    
    for i in range(2,m):
        for j in range(2,n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
            
    return grid[m-1][n-1]

print(f"the step require for the grid is : {grid_dynamics(3,4)}")
logging.info(f"the step require for the grid is : {grid_dynamics(3,4)}")
