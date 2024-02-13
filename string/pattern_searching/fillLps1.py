'''
For Kmp algorithm need to create the lps array for it.
'''

def fullLps(str1):
    lps = [0] * len(str1)
    # return the array
    for i in range(len(str1)):
        i = i + 1
        lps[i] = longPropPreSuff(str1,i)
        
    return lps


# now the main part of the program
def longPropPreSuff(str1,n):
    for len in range(n-1,-1,-1):
        flag = True
        for i in range(len):
            if str1[i] != str1[n-len+i]:
                flag = False
        if flag == True:
            return len
        
        
# try to execute the function
str1 = "ababacab"
temp = fullLps(str1)
print(temp)