'''
Given two strings A and B, find if A is a subsequence of B. 
A subsequence is a sequence that can be derived from another sequence by deleting 
some elements without changing the order of the remaining elements.


Example 1:

Input:
A = AXY 
B = YADXCP
Output: False
Explanation: A is not a subsequence of B
as 'Y' appears before 'A'.

Example 2:

Input:
A = gksrek
B = geeksforgeeks
Output: True
Explanation: A is a subsequence of B.
'''
def checkSubSequence(str1,str2):
    m = len(str1)
    n = len(str2)
    i , j = 0 , 0
    while i < m and j < n :
        if str1[i] == str2[j]:
            i +=1
            j +=1
        else :
            j+=1
    return i == n


    
    
# testing the concept
str1 = "gksrek"
str2 = "geeksforgeeks"

print("subsequence ." if checkSubSequence(str1,str2)== 0 else "Not a subsequence.")