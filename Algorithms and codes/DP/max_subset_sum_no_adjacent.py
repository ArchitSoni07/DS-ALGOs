def fun(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array
    maxSums = array[:]
    maxSums[1] = max(array[0],array[1])
    for i in range(2,len(array)):
        maxSums[i] = max(maxSums[i-1],(maxSums[i-2]+array[i]))
    return maxSums[-1]
    

def fun(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array
    second = array[0]
    first = max(array[0],array[1])
    for i in range(2,len(array)):
        current = max(first,second+array[i])
        second = first
        first = current
    return first

print(fun([7,10,12,7,9,14]))