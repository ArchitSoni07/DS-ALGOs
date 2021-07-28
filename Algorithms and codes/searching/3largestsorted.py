def fun(array):
    threelargest = [None,None,None]
    for num in array:
        updateLargest(threelargest,num)
    return threelargest

def updateLargest(threelargest,num):
    if threelargest[2] is None or num > threelargest[2]:
        shiftAndUpdate(threelargest,num,2)
    elif threelargest[1] is None or num > threelargest[1]:
        shiftAndUpdate(threelargest,num,1)
    elif threelargest[0] is None or num > threelargest[0]:
        shiftAndUpdate(threelargest,num,0)

def shiftAndUpdate(array,num,idx):
    for i in range(idx+1):
        if i==idx:
            array[i] = num
        else:
            array[i] = array[i+1]