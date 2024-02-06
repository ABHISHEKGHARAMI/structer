'''
Problem: Given two strings, check whether two strings are an anagram of each other.
Two strings are said to be an anagram of each other if they are just permutations of each other. 
That is, the set of characters in both the strings must be the same, only the order of characters
can be different.

'''
from collections import Counter

def checkAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        flag = 0
        c1 = Counter(str1)
        c2 = Counter(str2)
        for i in c1:
            if c1[i] != c2[i]:
                flag = 1
                break
        if flag == 0:
            return True
        return False
        
        
# checking the function
str1 = "abcd"
str2 = "dbca"
print("Anagram." if checkAnagram(str1,str2)==True else "Non Anagram.")