def fun(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num,maxEndingHere+num)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar

print(fun([10,15,20,30,40,-90]))

#O(n)
#o(1)