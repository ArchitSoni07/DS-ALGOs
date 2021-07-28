def fun(array):
    minOutofOrder = float("inf")
    maxOutofOrder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutofOrder(i,num,array):
            minOutofOrder = min(minOutofOrder,num)
            maxOutofOrder = max(maxOutofOrder,num)
    if minOutofOrder == float('inf') or maxOutofOrder == float('inf'):
        return [-1,-1]
    subArrayLeftIdx = 0
    while minOutofOrder >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array)-1
    while maxOutofOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx,subArrayRightIdx]


def isOutofOrder(i,num,array):
    if i == 0:
        return num > array[i+1]
    if i == len(array)-1:
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]

print(fun([1,2,4,7,10,11,7,12,6,7,16,18,19]))