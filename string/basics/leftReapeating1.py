'''
You are given a string S (both uppercase and lowercase characters). 
You need to print the repeated character whose first appearance is leftmost.

Example 1:

Input:
S = geeksforgeeks
Output: g
Explanation: We see that both e and g
repeat as we move from left to right.
But the leftmost is g so we print g.

'''

from collections import Counter

def leftReapeating(str1):
    if len(str1) == 0:
        return ""
    else:
        ans =""
        temp = list(str1)
        c1 = Counter(str1)
        for i in range(len(temp)):
            if temp[i] in c1 and c1[temp[i]] > 1:
                ans+=temp[i]
                break
        return ans
    
    
# inspecting the main fucntion
str1 = "geeksforgeeks"
print(f"the left most repeating charecter is : {leftReapeating(str1)}")
        