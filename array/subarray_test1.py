# print all the subarray of the given array
def subarray(arr,start,end):
    if len(arr)==end:
        return
    if start > end:
        return subarray(arr,start+1,end)
    else:
        print(arr[start:end+1])
        subarray(arr,0,end+1)
        