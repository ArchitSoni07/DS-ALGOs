def bubblesort(array):
    isSorted = False
    while not isSorted:
        isSorted = True    
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swap(i,i+1,array)
                isSorted = False
    return array


def swap(i,j,array):
    array[i],array[i+1] = array[i+1],array[i]

print(bubblesort([55,10,2,318,7,199,123456]))            

