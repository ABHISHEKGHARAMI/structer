def subset(arr,start,end):
    if len(arr) == end:
        return 
    if start > end:
        return subset(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return subset(arr,start+1,end)
    
    
# print all the subset of the array

list1 = [1,2,3,4]
subset(list1,0,0)
        