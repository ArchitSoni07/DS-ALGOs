def hasSingleCycle(array):
    numElementsVisited = 0
    CurrebtIndex = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and CurrebtIndex == 0:
            return False
        numElementsVisited += 1
        CurrebtIndex = getNextIndex(CurrebtIndex,array)
    return CurrebtIndex == 0

def getNextIndex(CurrebtIndex,array):
    jump = array[CurrebtIndex]
    nextIndex = (CurrebtIndex+jump) % len(array)
    return nextIndex if nextIndex >= 0 else nextIndex+len(array)

print(hasSingleCycle([2,3,1,-4,-4,2]))

