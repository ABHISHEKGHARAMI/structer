# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()


'''
Problem statement : You have supplied to the m * n grids to go , find the number of the moves where 
you can go from start to end.
'''

# recursive call for that
def getGridrec(m,n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    else:
        return getGridrec(m-1,n) + getGridrec(m,n-1)
    
    
m,n = int(input("enter the number of the row and column for the grid :").split(','))

print(f"The move for this path is : {getGridrec(m,n)}")
logging.info(f"The move for this path is : {getGridrec(m,n)}")
    