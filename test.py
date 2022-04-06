
def first_non_consecutive(arr):
    y = arr[0]
    for x in arr:
        if x != y:
            return x
        y +=1
    
print(first_non_consecutive([1,2,3,4,6,7,8]))


