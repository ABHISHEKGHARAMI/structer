'''
Given a string str and another string patt. 
Find the minimum index of the character in str that is also present in patt.


Example 1:

Input:
str = geeksforgeeks
patt = set
Output: 1
Explanation: e is the character which is
present in given str "geeksforgeeks"
and is also present in patt "set". Minimum
index of e is 1. 

'''

def minIndexingChar(Str1,patt):
    if len(Str1) == 0:
        return ""
    else:
        temp = list(Str1)
        dict1 = {}
        for i in range(len(temp)):
            if temp[i] not in dict1:
                dict1[temp[i]] = i
            else:
                if dict1[temp[i]] > i:
                    dict1[temp[i]] = i
                    
        # then compare with the pattern
        min = 99999
        str2 = ""
        for i in patt:
            if i in dict1:
                if dict1[i] < min:
                    str2 += i
                    min = dict1[i]
        return min
    


# checking the main function

str1 = "geeksforgeeks"
patt = "set"

print(f"The minimum charecter of the pattern is : {minIndexingChar(str1,patt)}")