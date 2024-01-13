'''Given two sorted arrays, a[] and b[], the task is to find the median of
these sorted arrays, where N is the number of elements in the first array, 
and M is the number of elements in the second array. 

Input: a[] = {-5, 3, 6, 12, 15}, b[] = {-12, -10, -6, -3, 4, 10}
Output: The median is 3.
Explanation: The merged array is: ar3[] = {-12, -10, -6, -5 , -3, 3, 4, 6, 10, 12, 15}.
So the median of the merged array is 3'''
def madian1(m,n):
    s = []
    s.append(m)
    s.append(n)
    s.sort()
    n = len(s)
    if n %2 == 0:
        return (s[n//2] + s[(n+1)//2])//2
    else:
        return s[(n+1)//2]
    
a1 = [-5, 3, 6, 12, 15]
a2 = [-12, -10, -6, -3, 4, 10]

print(f"The median of this is : {madian1(a1,a2)}")