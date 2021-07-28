def fun(array):
    subset = [[]]
    for element in array:
        for i in range(len(subset)):
            currentSet = subset[i]
            subset.append(currentSet+[element])
    return subset

print(fun([1,2,3]))

#Time = O((2^n) * n)
#Space = O((2^n) * n)