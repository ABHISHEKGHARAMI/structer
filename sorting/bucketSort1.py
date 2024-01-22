'''

Bucket sort algorithm 
unstable algorithm :

1. first get the max and min element of the array .
2. create empty bucket
3. insert the element according to the calculation.
4. sort each of the bucket.
5. return the result.


'''


def bucketSort(arr):
    n = len(arr)
    max1 = max(arr)
    min1 = min(arr)
    # calculating the bucket list
    bucket_range = (max1 - min1) / n
    
    #creating the bucket
    buckets = [[] for _ in range(n+1)]
    
    # distributing the array element according to calculation
    for num in arr:
        index = int((num - min1)/bucket_range)
        buckets[index].append(num)
    
    # sort the buckets
    sorted_bucket = [ sorted(bucket) for bucket in buckets]
    
    # concentretate the result
    result = [ num for bucket in sorted_bucket for num in bucket]
    
    # return the result
    return result


# main function
arr = [3.2, 1.8, 0.5, 4.3, 2.1, 3.8]
print(f"after sorting that the array will be : {bucketSort(arr)}")