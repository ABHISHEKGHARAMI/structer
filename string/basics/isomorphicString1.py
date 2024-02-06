'''
Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.

If the characters in str1 can be changed to get str2, then two strings, str1 and str2,
are isomorphic. A character must be completely swapped out for another character while maintaining
the order of the characters. A character may map to itself, but no two characters may map to 
the same character.

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 
1
'''
from collections import Counter

def checkIsomorphic(str1,str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    fre1 = list(c1.values())
    fre2 = list(c2.values())
    flag = 0
    for i in range(len(fre1)):
        if fre1[i] != fre2[i]:
            flag = 1
            break
    if flag == 0:
        return 1
    return 0


# the main function
str1 = 'aab'
str2 = 'xyy'

print("Isomorphic String" if checkIsomorphic(str1,str2) == 1 else "Not Isomorphic String")