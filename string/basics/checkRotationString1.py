# check  for the rotation of the string
def checkRotation(s1,s2):
    s3  = s1 + s1
    if s2 in s3:
        return 1
    else:
        return 0
    
    
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

print("String contains rotation." if checkRotation(str1,str2)==1 else "String Does not contain rotation.")