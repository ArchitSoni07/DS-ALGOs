def Node:
    def __init__(self,name):
        self.children = []
        self.name = name
    def addchild(self,name):
        self.children.append(Node(name))

    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array