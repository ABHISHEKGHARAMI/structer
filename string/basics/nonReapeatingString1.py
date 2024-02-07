# print the non repeating charecter of a string

from collections import Counter

def nonRepeating(str1):
    if len(str1) == 0:
        return ""
    else:
        c1 = Counter(str1)
        ans = ""
        for i in c1:
            if c1[i] == 1:
                ans+= i
                break
            
        return ans
    
    
# checking the function

str1 = "hello"

print(f"The non repeating charecter of the string is : {nonRepeating(str1)}")