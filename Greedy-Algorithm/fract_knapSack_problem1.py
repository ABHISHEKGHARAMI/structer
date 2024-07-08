"""
Problem Statement :
Given the weights and profits of N items, in the form of {profit, weight} put
these items in a knapsack of capacity W to get the maximum total profit in the knapsack.

"""


# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

# class for item
class Item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight
        

# solving the problem for the locally tends to the globally
def knapSackSolution(w,arr):
    # first sort the arr using the profit and weight ratio
    arr.sort(key=lambda x : (x.profit/x.weight),reverse=True)
    
    final_output = 0.0
    
    # looping through the arr
    for item in arr:
        # check the weight is overflowing or not
        if item.weight <= w:
            w = w - item.weight
            final_output += item.profit
            
        else:
            # if we can do that then we go for the partially breaking the item in to fraction
            final_output += item.profit * w / item.weight
            
    # finally return the profit
    return final_output

# main execution of the problem
W = 50
arr = [Item(60, 10), Item(100, 20), Item(120, 30)]

max_profit = knapSackSolution(W,arr)

print(f"The maximum profit of the problem is :{max_profit}")
logging.info(f"The maximum profit of the problem is :{max_profit}")
