'''

Ternary Search is a Divide and Conquer Algorithm used to perform search operation in a sorted array.
This algorithm is similar to the Binary Search algorithm but rather than dividing the array 
into two parts, it divides the array into three equal parts.

In this algorithm, the given array is divided into three parts and the key (element to be searched)
is compared to find the part in which it lies and that part is further divided into three parts.

We can divide the array into three parts by taking mid1 and mid2 which can be 
calculated as shown below. Initially, l and r will be equal to 0 and N-1 respectively,
where N is the length of the array.


'''

def ternarySearch(arr,low,high,x):
    if low <= high:
        mid1 = low + (high - 1) // 3
        mid2 = high - (high - 1) // 3
        
        if arr[mid1] == x :
            return mid1
        
        if arr[mid2] == x:
            return mid2
        
        elif arr[mid1] > x:
            return ternarySearch(arr,low,mid1,x)
        elif arr[mid1] < x and arr[mid2] > x:
            return ternarySearch(arr,mid1+1,mid2-1,x)
        else:
            return ternarySearch(arr,mid2+1,end,x)
        
    else:
        return -1

arr = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
x = 130
pos = ternarySearch(arr,0,len(arr)-1,x) 

if pos!=-1:
    print(f"The {x} is present at the position of : {pos}")
else:
    print(f"The {x} is not present in the array.")