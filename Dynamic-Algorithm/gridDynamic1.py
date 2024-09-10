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
    
    
# Dynamic solution for the grid problem
def getGridDynamic(m,n,mem={}):
    key = f"{m},{n}"
    if key not in mem:
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        else:
            mem[key] = getGridDynamic(m-1,n,mem) + getGridDynamic(m,n-1,mem)
    return mem[key]
        
    
    
m,n = map(int,input("enter the row and column :").split(','))

print(f"The move for this path is : {getGridrec(m,n)}")
logging.info(f"The move for this path is : {getGridrec(m,n)}")



print(f"The move using the dynamic solution is : {getGridDynamic(m,n)}")
logging.info(f"The move using the dynamic solution is : {getGridDynamic(m,n)}")
    