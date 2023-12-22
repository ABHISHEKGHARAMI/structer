'''
Given two integer arrays of the same size, “arr[]” and “index[]”, 
reorder elements in “arr[]” according to the given index array.
'''

def reorder(arr,index):
    res = [0]*len(index)
    if len(arr)==len(index):
        for i in range(len(index)):
            res[i] = arr[index[i]]
            
        print(res)
        
    else:
        return 
    
    
# main function
arr  = [10, 11, 12]
index = [1, 0, 2]

reorder(arr,index)
        