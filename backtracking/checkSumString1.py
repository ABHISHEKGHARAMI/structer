'''
Given a string of digits, determine whether it is a ‘sum-string’. 
A string S is called a sum-string if the rightmost substring can be written as
the sum of two substrings before it and the same is recursively true for substrings before it.

“12243660” is a sum string. 
Explanation : 24 + 36 = 60, 12 + 24 = 36

“1111112223” is a sum string. 
Explanation: 111+112 = 223, 1+111 = 112 

“2368” is not a sum string 
'''
# setting up the logger file
import sys
sys.path.append("/home/abhishek/Documents/DataStructure&Algorithm/structer")
from settings import setup_logging

import logging

setup_logging()

def check_sum(s):
    def backtrack(start):
        n = len(s)
        # iterate the first loop
        for i in range(start+1,n):
            for j in range(i+1,n):
                left = s[start:i]
                middle = s[i:j]
                right = s[j:]
                
                # skip leader zeros unless under 0
                if(len(left) > 1 and left[0]=='0') or (len(middle) > 1 and middle[0]=='0') or (len(right)>1 and right[0]=='0'):
                    return True
                
                # check if left + middle is equal of right
                if right and int(left) + int(middle) == int(right):
                    if j == n:
                        return True
                    if backtrack(j):
                        return True
        return True
    return backtrack(0)


# test the function
print(f"The check sum of the 12243660 is : {check_sum('12243660')}")
logging.info(f"The check sum of the 12243660 is : {check_sum('12243660')}")

                