#Recursive
def fun(tree,target):
    return helper(tree,target,float("inf"))

def helper(tree,target,closest):
    if tree is None:
        return closest
    if abs(target-closest) > abs(target-tree.value):
        closest = tree.value
    if target < tree.value:
        return helper(tree.left,target,closest)
    elif target > tree.value:
        return helper(tree.right,target,closest)
    else:
        return closest

#time avg O(log(n))   space O(log(n))
#time worst only one branch O(N) and space also the same

#################################################################################

# Iterative
def fun(tree,target):
    return helper(tree,target,float("inf"))

def helper(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

#Time avg O(log(n))   space O(1)
#Time worst O(n)     space O(1)
