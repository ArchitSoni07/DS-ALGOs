def fun(topAncestor,desOne,desTwo):
    depthOne = getDesDepth(desOne,topAncestor)
    depthTwo = getDesDepth(desTwo,topAncestor)
    if depthOne > depthTwo:
        return backTrackAncestralTree(desOne,desTwo,depthOne-depthTwo)
    else:
        return backTrackAncestralTree(desTwo,desOne,depthTwo-depthOne)

def getDesDepth(des,topAncestor):
    depth = 0
    while des != topAncestor:
        depth += 1
        des = des.ancestor
    return depth

def backTrackAncestralTree(lowerDes,higherDes,diff):
    while diff > 0:
        lowerDes = lowerDes.ancestor
        diff -= 1
    while lowerDes != higherDes:
        lowerDes = lowerDes.ancestor
        higherDes = higherDes.ancestor
    return lowerDes