'''
Given a string str containing alphanumeric characters.
The task is to calculate the sum of all the numbers present in the string.

Example 1:

Input:
str = 1abc23
Output: 24
Explanation: 1 and 23 are numbers in the
string which is added to get the sum as
24.

'''
def sumAlphaNumeric(Str1):
    total_sum = 0
    current_sum = 0
    for char in Str1:
        if char.isdigit():
            current_sum = current_sum * 10 + int(char)
        else:
            total_sum += current_sum
            current_sum = 0
    total_sum += current_sum
    return total_sum


str1 = "1abc23"
print(f"The total sum of the alpha numeric charecter : {sumAlphaNumeric(str1)}")