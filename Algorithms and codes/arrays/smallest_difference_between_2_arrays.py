def fun(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstnum = arrayOne[idxOne]
        secondnum = arrayTwo[idxTwo]
        if firstnum < secondnum:
            current = secondnum - firstnum
            idxOne += 1
        elif secondnum < firstnum:
            current = firstnum-secondnum
            idxTwo += 1
        else:
            return [firstnum,secondnum]
        if smallest > current:
            smallest = current
            smallestPair = [firstnum,secondnum]
    return smallestPair

print(fun([10,20,30,40,50,60,70,80],[100,200,300,400,500,600,700,800,900,11]))