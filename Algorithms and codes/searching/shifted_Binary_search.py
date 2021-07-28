def fun(array,target):
    SBSHelper(array,target,0,len(array)-1)

def SBSHelper(array,target,left,right):
    if left > right:
        return -1
    middle = (left+right)//2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]
    if target == potentialMatch:
        return middle
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            SBSHelper(array,target,left,middle-1)
        else:
            SBSHelper(array,target,middle+1,right)
    else:
        if target > potentialMatch and target <= rightNum:
            SBSHelper(array,target,middle+1,right)
        else:
            SBSHelper(array,target,left,middle-1)
    