# checking the pallindome for a string
def checkPallindrome(str1):
    str2 = str1[::-1]
    if str1 == str2 :
        return 1
    else:
        return 0
    
    
str1 = "aaabbbaaa"
print("Pallindrome" if checkPallindrome(str1) == 1 else "Not a Pallindrome.")