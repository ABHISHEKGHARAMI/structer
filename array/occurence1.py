'''
Given an array of N numbers and a positive integer K. 
The problem is to find K numbers with the most occurrences, 
i.e., the top K numbers having the maximum frequency.
If two numbers have the same frequency then the number with a larger value
should be given preference. 
The numbers should be displayed in decreasing order of their frequencies
. It is assumed that the array consists of at least K numbers.Given an array of N 
numbers and a positive integer K. The problem is to find K numbers
with the most occurrences, i.e., the top K numbers having the maximum frequency. 
If two numbers have the same frequency then the number with a larger
value should be given preference. 
The numbers should be displayed in decreasing order of their frequencies.
It is assumed that the array consists of at least K numbers.
'''

from collections import Counter


def frequency(arr,k):
    # use the counter
    freq_cont = Counter(arr)
    
    # sort the element based on the frequency 
    sorted_element = sorted(freq_cont.items(), key = lambda x: (-x[1],x[0]))
    
    # take the k element from the sorted_element
    
    res = [element[0] for element in sorted_element[:k]]
    
    return res


    
    
arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]

res = frequency(arr,4)
if res[0] == 0:
    print("No element match the frequency.")
else:
    for i in res:
        print(i,end=" ")