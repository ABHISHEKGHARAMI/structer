'''
Given a string S of lowercase alphabets, check if it is isogram or not.
An Isogram is a string in which no letter occurs more than once.

Example 1:

Input:
S = machine
Output: 1
Explanation: machine is an isogram
as no letter has appeared twice. Hence
we print 1.

'''
from collections import Counter

def isoGram(str1):
    c1 = Counter(str1)
    flag = 0
    for i in c1:
        if c1[i] != 1:
            flag = 1
            break
    if flag == 1:
        return 0
    return 1


# checking the function
str1 = "abcd"
print("Isogram ." if isoGram(str1) == 1 else "Not Isogram .")
    