def swap(i,j,array):
    array[i],array[j] = array[j],array[i]
def quicksort(array):
    quicksortHelper(array,0,len(array)-1)
    return array

def quicksortHelper(array,startidx,endidx):
    if startidx >= endidx:
        return
    pivotidx = startidx
    leftidx = startidx+1
    rightidx = endidx
    while rightidx >= leftidx:
        if array[leftidx] > array[pivotidx] and array[rightidx] < array[pivotidx]:
            swap(leftidx,rightidx,array)
        if array[leftidx] <= array[pivotidx]:
            leftidx += 1
        if array[rightidx] >= array[pivotidx]:
            rightidx -= 1
    swap(pivotidx,rightidx,array)
    leftsubAisSMALL = rightidx-1-startidx < endidx-(rightidx+1)
    if leftsubAisSMALL:
        quicksortHelper(array,startidx,rightidx-1)
        quicksortHelper(array,rightidx+1,endidx)
    else:
        quicksortHelper(array,rightidx+1,endidx)
        quicksortHelper(array,startidx,rightidx-1)


print(quicksort([45,894,368,445,1234,7841,1]))
