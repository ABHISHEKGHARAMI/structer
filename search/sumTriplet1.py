# find the sum using the triplet
# arr = [2,3,4,8,9,10,20,40] sum = 32

def findTriplet(arr,target_sum):
    n = len(arr)
    
    for i in range(n-2):
        compilent_set = set()
        current_sum = target_sum - arr[i]
        
        for j in range(i+1,n):
            if target_sum - arr[j] in compilent_set:
                return True
            compilent_set.add(arr[j])
    return False

arr = [1, 4, 2, 8, 3, 9]
target_sum = 15
if findTriplet(arr,target_sum) == True:
    print("pair exist")
else:
    print("pair does not exist")

