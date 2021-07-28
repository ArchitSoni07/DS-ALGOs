def ss(array):
    currentidx = 0
    while currentidx < len(array)-1:
        smallestidx = currentidx
        for i in range(currentidx+1,len(array)):
            if array[smallestidx] > array[i]:
                smallestidx = i
            swap(currentidx,smallestidx,array)
            currentidx += 1
    return array

def swap(i,j,array):
    array[i],array[j] = array[j],array[i]
print(ss([45,78,63,258,446]))


