def inOrderTraverse(tree,array):
    if tree is not None:
        inOrderTraverse(tree.left,array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    return array

def preOrder(tree,array):
    if tree is not None:
        array.append(tree.value)
        preOrder(tree.left,array)
        postOrder(tree.right,array)
    return array

def postOrder(tree,array):
    if tree is not None:
        postOrder(tree.left,array)
        postOrder(tree.right,array)
        array.append(tree.value)
    return array