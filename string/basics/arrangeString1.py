'''
Given a string S consisting of only uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.

Example 1:

Input:
N = 12
S = defRTSersUXI
Output: deeIRSfrsTUX
Explanation: Sorted form of given string
with the same case of character as that
in original string is deeIRSfrsTUX

'''
def arrangeString(str1):
    if len(list(str1)) == 0:
        return ""
    else:
        l1 = list(str1)
        lower = []
        upper = []
        for i in range(len(l1)):
            if l1[i].isupper() == True:
                upper.append(l1[i])
            else:
                lower.append(l1[i])
        lower.sort()
        upper.sort()
        
        new_string = ""
        j , k = 0 , 0
        for i in range(len(l1)):
            if l1[i].isupper() == True:
                new_string+=upper[j]
                j+=1
            else:
                new_string += lower[k]
                k+=1
        return new_string
    
    
    
# checking the function

str1 = "defRTSersUXI"
print(f"The rearrange string is : {arrangeString(str1)}")
            
            