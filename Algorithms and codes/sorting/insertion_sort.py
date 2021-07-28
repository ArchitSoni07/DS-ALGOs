def insertionsort(array):
    for i in range(1,len(array)):
        while array[i] > array[i-1] and i>0:
            swap(i,i-1,array)
            i -= 1
    return array

def swap(i,j,array):
    array[i],array[j] = array[j],array[i]

print(insertionsort([10,85,2,3,45,97]))