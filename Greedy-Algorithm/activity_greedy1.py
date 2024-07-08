# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

"""
problem statement :
You are given n activities with their start and finish times. 
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time. 
"""

def activity_selector(s,f):
    try:
        # first task will always will be selected
        n = len(f)
        print("the following activity will be selected :")
        logging.info("the following activity will be selected :")
        i = 0
        print(i)
        logging.info(i)
        # this is the greedy selector and locally optimize problem solution leading to the global solution.
        for j in range(1,n):
            if s[j]>=f[i]:
                print(j,end=" ")
                logging.info(j)
                i=j
    except Exception as e:
        print(e)
        logging.info(e)
        raise e
    

# execution of the program
s = [1, 3, 0, 5, 8, 5]  # starting 
f = [2, 4, 6, 7, 9, 9]  # finishing


activity_selector(s,f)