class TSTNode:
    #constructor: this method receives the key, the value, the left node, the right node and the parent node
    def __init__(self, id, name, party, x = 0, y = 0, leftChild=None, middleChild=None, rightChild=None, parentNode=None):
        self.id = id
        self.name = name
        self.party = party
        self.leftChild = leftChild
        self.middleChild = middleChild
        self.rightChild = rightChild
        self.parentNode = parentNode
        self.x = x
        self.y = y


    def hasParentNode(self):
        return self.parentNode

    #This method verifies if the current node has a child node on the left
    def hasLeftChild(self):
        return self.leftChild
    
    #This method verifies if the current node has a child node on the middle
    def hasMiddleChild(self):
        return self.middleChild
    
    #This method verifies if the current node has a child node on the right
    def hasRightChild(self):
        return self.rightChild

    def getNumChilds(self):
        num=0
        if(self.leftChild):
            num += 1
        if(self.middleChild):
            num += 1
        if(self.rightChild):
            num += 1
        return num

    def whatChildIs(self,sonID):
        pos=None
        if(sonID == self.leftChild.id):
            print("ES HIJO IZQUIERDO")
            pos=0
            return pos
        if(sonID == self.middleChild.id):
            print("ES HIJO MEDIO")
            pos=0
            return pos
        if(sonID == self.rightChild.id):
            print("ES HIJO DERECHO")
            pos=0
            return pos
    
    #This method verifies if self node is left child of other one
    def isLeftChild(self):
        return self.parentNode and self.parentNode.leftChild == self
    
    #This method verifies if self node is middle child of other one
    def isMiddleChild(self):
        return self.parentNode and self.parentNode.middleChild == self
    
    #This method verifies if self node is right child of other one
    def isRightChild(self):
        return self.parentNode and self.parentNode.rightChild == self
    
    #This method verifies if self node is lthe main root of the tree
    def isRoot(self):
        return not self.parentNode
    
    #This method verifies if self node is a leaf
    def isLeaf(self):
        return not (self.leftChild or self.rightChild or self.middleChild)
    
    #This method verifies if self node has at least one child
    def hasSomeChild(self):
        return (self.rightChild or self.leftChild or self.middleChild)
    
     #This method verifies if self node has both children
    def hasAllChilds(self):
        return (self.rightChild and self.leftChild and self.middleChild)
    
    #This method update the node information (key, value and children)
    def updateNodeInformation(self, key, name, leftChild, middleChild, rightChild):
        self.key = key
        self.name = name
        self.leftChild = leftChild
        self.middleChild = middleChild
        self.rightChild = rightChild
        if(self.hasRightChild()):
            self.rightChild.parentNode = self
        if(self.hasMiddleChild()):
            self.middleChild.parentNode = self
        if(self.hasLeftChild()):
            self.leftChild.parentNode = self