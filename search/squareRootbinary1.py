'''
Given an integer X, find its square root. If X is not a perfect square, then return floor(√x).

Examples : 

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.


'''

def sqaure(x):
    if x == 0 or x == 1:
        return x
    else:
        start = 1
        end = x//2
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x :
                start = mid + 1
                ans = mid
            else:
                end = end -1
        return ans


x = int(input("enter a number to find the root :"))  
print(f"The square root of {x} is : {sqaure(x)}")
                
            