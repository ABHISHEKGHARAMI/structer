# find the maximum occuring charecter
from collections import Counter

# using the counter
def maxChar(str1):
    if len(str1)!=0:
        c1 = Counter(str1)
        max_char =""
        count = 0
        for i in c1:
            if c1[i] >= count:
                count = c1[i]
                max_char += i
        c2 = list(max_char)
        c2.sort()
        return c2[0]
    
    
str1 = "testsample"
print(f"The most occuring charecter is : {maxChar(str1)}")