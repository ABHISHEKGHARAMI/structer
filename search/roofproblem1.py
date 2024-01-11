"""

You are given heights of consecutive buildings. 
You can move from the roof of a building to the roof of next adjacent building.
You need to find the maximum number of consecutive steps you can put 
forward such that you gain an increase in altitude with each step.

Example 1:

Input:
N = 5
A[] = {1,2,2,3,2}
Output: 1
Explanation: 1, 2 or 2, 3 are the only consecutive 
buildings with increasing heights thus maximum number
of consecutive steps with increase in gain in altitude
would be 1 in both cases.

"""

# naive solution
def naive_solution(arr):
    sum = 0
    for i in range(len(arr)-1):
        sum+= arr[i+1] - arr[i]
      
    return sum

arr = [1,2,3,4]
print(f"The minimum step is required is :{naive_solution(arr)}")