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

