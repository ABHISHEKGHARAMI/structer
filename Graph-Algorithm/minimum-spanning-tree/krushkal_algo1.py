# setting up the logger
import sys
sys.path.append("D:/geeks1.0/structer")
from settings import setup_logging
import logging
setup_logging()

'''
Problem statement :

using krushkal algorithm find the mst of the graph
steps 
1. first sort the graph with edge
2. then apply apply the union find algo to detect the cycle init then add the edge

'''

class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    
    
    # find the parent
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    
    
    # union of the two different parent to avoid cycle
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
                
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1