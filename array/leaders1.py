'''

Write a program to print all the LEADERS in the array. 
An element is a leader if it is greater than all the elements to its right side. 
And the rightmost element is always a leader. 

'''


# efficient approach for the leader problem
def leaders(arr):
    n = len(arr)
    le1 = []
    max_leader = arr[n-1]
    le1.append(arr[n-1])
    i = n-2
    while i >= 0 :
        if max_leader < arr[i]:
            max_leader = arr[i]
            le1.append(max_leader)
        i = i -1
        
    le1.reverse()
    print(le1)
                

ar = [16, 17, 4, 3, 5, 2]
leaders(ar)