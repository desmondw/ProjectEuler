import re

class Tree():
    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None
        self.data = None

#fill tree with provided data
def importTree(filepath):
    open(filepath)

    #convert to array
    treeList = []
    for line in file:
        treeList.append(re.split("\s", line))

    #convert to tree
    tree = Tree(None)
    for i in range(treeList):
        if i == 1:
            tree.
        for j in range(treeList[i]):


tree = importTree("18_data.txt")



#search tree for largest path sum
#revise code for non-brute force