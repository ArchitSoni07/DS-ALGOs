def BinarySearch(array,target):
    return BShelper(array,target,0,len(array)-1)

def BShelper(array,target,left,right):
    while left <= right:
        middle = (left+right)//2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            return BShelper(array,target,left,middle-1)
        else:
            return BShelper(array,target,middle+1,right)
    return -1
print(BinarySearch([12,45,78,96,358,624,786,954,123],96))