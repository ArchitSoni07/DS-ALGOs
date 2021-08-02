
# Given an array find the increasing sub sequence which has maximum sum
# [ 8, 12, 2, 3, 15, 5, 7 ]
# ans -> 8, 12, 15 = 35
# SPACE = O(n)  # Time = O(n^2)


def fun(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0,i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array,sequences,maxSumIdx)]

def buildSequence(array,sequences,currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx] 
    return list(reversed(sequence))

print(fun([845, 18482, 652, 22223, 56915, 5, 7]))