def push(arr,data):
    if data==None:
        return
    else:
        arr.append(data)
        print("Data Pushed.")
        
        
def insert(arr,pos,data):
    if pos< 0 and pos > len(arr):
        print("No place to add data in array")
    else:
        arr.insert(pos,data)
        
def pop(arr):
    if arr==None:
        return 0
    else:
        return arr.pop()
    
def search(arr,data):
    if data is None:
        return
    else:
        for i in range(len(arr)):
            if arr[i] == data:
                return 1
            
arr = [1,2,3,4]
push(arr,8)