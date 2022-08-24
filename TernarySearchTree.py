from Nodo import TSTNode
from uniones import Union

class TST:
    paths = ""
    arrayPaths = []
    arrayNodesLevel = []

    #Constructor: this constructor doesn't receives parameters
    def __init__(self):
        self.root = None
        self.weight = 0
        
    def weight(self):
        return self.weight
    
    def __len__(self):
        return self.weight
    
    def __setitem__(self, key, value):
        self.addNode(key, value)
    
    #This method verifies if a tree exists, then the node is added as a root or as a child node
    def addNode(self, key, name, party, fatherkey):
        if(self.root): # The tree root exists! then, the node is added as a child
            if fatherkey == 0: #If the father is 0, the node to add is the root
                self._addNode(key, name, self.root)
            else: #father diferent to 0
                currentNode = self.getNode(self.root, fatherkey)#get the node father
                if currentNode: #Node father found
                    self._addNode(key, name, party, currentNode) #add the child
                else:#Node father not found
                    print("Nodo ", fatherkey, "no encontrado")
        else: # The tree haven't a root, then the node is added as main root
            self.root = TSTNode(key, name, party)
            print("The node " + str(name) + " has been added as the main root.")
        self.weight += 1
    
    def _addNode(self, id, name, party, currentNode):
        # As a TST, the childs need to be add to the left, middle and right
        if(currentNode.isLeaf()): #if this is a leaf add the node to the left
            currentNode.leftChild = TSTNode(id, name, party, parentNode=currentNode) #add
            print("The node " + str(name) + " has been added as left child of " + str(currentNode.name)) #show
        else:
            if not currentNode.hasRightChild(): #if this doesnt have right child possibly doesnt have middle child
                if not currentNode.hasMiddleChild(): #doesnt have middle child, lets add
                    currentNode.middleChild = TSTNode(id, name, party, parentNode=currentNode)#add
                    print("The node " + str(name) + " has been added as middle child of " + str(currentNode.name))#show
                else:#have middle child, lets add node as right child
                    currentNode.rightChild = TSTNode(id, name, party, parentNode=currentNode) #add 
                    print("The node " + str(name) + " has been added as right child of " + str(currentNode.name)) #show
            else:
                print("The node " + str(name) + " can't be added as a child of " + str(currentNode.name)) #
    
    #Get node by key
    def getNode(self, root, id):
        if(root): #root exists
            node = self._getNode(root, id) #search the node by id
            if node: #if find the node
                return node #return the node
        else:
            return None 
    
    def _getNode(self,currentNode,id):
        nod = None
        if currentNode: #node diferent to None
            if currentNode.id==id: #id node equals to id to seach
                nod = currentNode #assing the node
                return nod #return
            else: #id diferent
                if nod==None:
                    nod=self._getNode(currentNode.leftChild,id) #go the left child
                if nod==None:
                    nod=self._getNode(currentNode.middleChild,id) #go the middle child
                if nod==None:
                    nod=self._getNode(currentNode.rightChild,id) #go the right child
        return nod

    def delNode(self, root, id):
        print("\n___Deleting Node__")
        if(root): #root exists
            node = self.getNode(root, id) #search the node by id
            return self._delNode(node)
        else:
            return None

    def _delNode(self, currentNode):
        bool = False
        findbool = False
        
        if(currentNode.isLeaf()): #Leaf
            if(currentNode.isLeftChild()):
                print(currentNode.id, "era hoja hijo izquierdo de", currentNode.parentNode.id)
                currentNode.parentNode.leftChild = None
                if(currentNode.parentNode.hasMiddleChild()):
                    currentNode.parentNode.leftChild = currentNode.parentNode.middleChild
                    currentNode.parentNode.middleChild = None
                if(currentNode.parentNode.hasRightChild()):
                    currentNode.parentNode.middleChild = currentNode.parentNode.rightChild
                    currentNode.parentNode.rightChild = None
                currentNode.parentNode = None
                bool = True
            elif(currentNode.isMiddleChild()):
                print(currentNode.id, "era hoja hijo medio de", currentNode.parentNode.id)
                currentNode.parentNode.middleChild = None
                if(currentNode.parentNode.hasRightChild()):
                    currentNode.parentNode.middleChild = currentNode.parentNode.rightChild
                    currentNode.parentNode.rightChild = None
                bool = True
            elif(currentNode.isRightChild()):
                print(currentNode.id, "era hoja hijo derecho de", currentNode.parentNode.id)
                currentNode.parentNode.rightChild = None
                bool = True
            currentNode.parentNode = None
        else: #No leaf
            if not(currentNode.leftChild.hasMiddleChild()): #Only left child of current.leftChild
                if(currentNode.hasRightChild()):
                    currentNode.rightChild.parentNode = currentNode.leftChild
                    currentNode.leftChild.rightChild = currentNode.rightChild
                    print(currentNode.leftChild.rightChild.id,"movido a",currentNode.leftChild.id)
                    currentNode.rightChild = None
                    bool = True
                if(currentNode.hasMiddleChild()):
                    currentNode.middleChild.parentNode = currentNode.leftChild
                    currentNode.leftChild.middleChild = currentNode.middleChild
                    print(currentNode.leftChild.middleChild.id,"movido a",currentNode.leftChild.id)
                    currentNode.middleChild = None
                    bool = True
            else: #currentNode.leftChild has more childs
                if(currentNode.hasAllChilds()): #All brothers
                    if(currentNode.leftChild.hasRightChild()):
                        self.findEmptyChild(currentNode.leftChild.rightChild,currentNode.rightChild,findbool)
                        currentNode.leftChild.rightChild = None
                    self.findEmptyChild(currentNode.leftChild.middleChild,currentNode.middleChild,findbool)
                    currentNode.leftChild.middleChild = None
                    
                    currentNode.middleChild.parentNode = currentNode.leftChild
                    currentNode.leftChild.middleChild = currentNode.middleChild
                    currentNode.middleChild = None
                    currentNode.rightChild.parentNode = currentNode.leftChild
                    currentNode.leftChild.rightChild = currentNode.rightChild
                    currentNode.rightChild = None
                    bool = True
                else: #only current.middleChild
                    if(currentNode.leftChild.hasRightChild()):
                        self.findEmptyChild(currentNode.leftChild.rightChild,currentNode.middleChild,findbool)
                        currentNode.leftChild.rightChild = None
                    self.findEmptyChild(currentNode.leftChild.middleChild,currentNode.middleChild,findbool)
                    currentNode.leftChild.middleChild = None
                    
                    currentNode.middleChild.parentNode = currentNode.leftChild
                    currentNode.middleChild = None
                    bool = True
            currentNode.leftChild.parentNode = currentNode.parentNode 
        if(currentNode == self.root):
            self.root = currentNode.leftChild
        if(currentNode.isLeftChild()):
            currentNode.parentNode.leftChild = currentNode.leftChild
            currentNode.leftChild = None
            bool = True
        elif(currentNode.isMiddleChild()):
            currentNode.parentNode.middleChild = currentNode.leftChild
            currentNode.leftChild = None
            bool = True
        elif(currentNode.isRightChild()):
            currentNode.parentNode.rightChild = currentNode.leftChild
            currentNode.leftChild = None
            bool = True
        return bool
        print("NODO ELIMINADO")
    findbool = False
    
    def findEmptyChild(self,hijoadop,padreadop,findbool):
        if(findbool):
            print(hijoadop.id,"reposition to",padreadop.id)
            return True
        if(padreadop):
            if(padreadop.isLeaf()):
                hijoadop.parentNode = padreadop
                padreadop.leftChild = hijoadop
                return True
            else:
                if not(padreadop.hasRightChild()):
                    if(padreadop.hasMiddleChild()):
                        padreadop.middleChild = hijoadop
                        padreadop.middleChild.parentNode = padreadop
                        findbool = True
                    else:
                        padreadop.rightChild = hijoadop
                        padreadop.rightChild.parentNode = padreadop
                        findbool = True
                else:
                    if(padreadop.hasLeftChild()):
                        findbool = self.findEmptyChild(hijoadop,padreadop.leftChild,findbool)
                    if(padreadop.hasMiddleChild()):
                        findbool = self.findEmptyChild(hijoadop,padreadop.middleChild,findbool)
                    if(padreadop.hasRightChild()):
                        findbool = self.findEmptyChild(hijoadop,padreadop.rightChild,findbool)
        return findbool

    def longerPath(self, root):#show the bigger path
        if(root): #root exits
            completPath = self._paths(root, self.arrayPaths, self.paths) #get array of paths (root to leafs)( [[5,2,1],[5,2,2]] )
            print(len(completPath))
            numNodos = 0
            for arregloCaminos in completPath: #walk in array ( [5,2,1] ) , ([5,2,2])
                i = 0
                for k in arregloCaminos: #walk in array ( 5 , 2 , 1 ) , ( 5 , 2 , 2 )
                    i += 1 #count amount of index
                if(numNodos < i): # compare max index and i
                    numNodos += 1 # set the max amount of index
                    camino = arregloCaminos #save the path
            print(camino) #show the path
            return camino #return the path
        else:
            print("El arbol no existe")
            return None
    
    def _paths(self, root, arreglo, caminos):#find all paths from foot to leaf
        if(root.isLeaf()):#save path in a array
            #print(str(root.id) + " hoja")
            caminos = caminos + str(root.id) + ";"#Add node id, to string
            #print(caminos)
            arreglo.append(caminos)#add string to array
        else:
            #print(str(root.id) + " no hoja")
            caminos = caminos + str(root.id) + ";"#Add node id, to string
            #print(caminos)
            if(root.hasLeftChild()):
                self._paths(root.leftChild, arreglo, caminos)#go recursive left child
            if(root.hasMiddleChild()):
                self._paths(root.middleChild, arreglo, caminos)#go recursive middle child
            if(root.hasRightChild()):
                self._paths(root.rightChild, arreglo, caminos)#go recursive right child
        arreglado = self.pathFixer(arreglo) #fix array from string to arrays
        return arreglado #return the array of paths
    
    #Fix Array of Strings to Array of Arrays
    def pathFixer(self, arrayPath):
        separatedArr = []
        
        #split elements separated by ";", like elements of array 
        for k in arrayPath:
            j = str(k)
            separatedArr.append(j.split(";"))
            
        #when do the split, there are elements that remain empty, this eliminates them
        for x in separatedArr:
            x.remove('') #remove empty indexs
        return separatedArr
                  
    def completeTree(self, root):
        completeBool = True #boolean of the method
        if root == None: #root doesnt exist
            return [] #exit of the method
        levels = self.getNodesByLevel(root) #get the array of nodes by levels
        i = 0
        for level in levels: #walk into levels array
            if(i < len(levels)-2):#goes to the antepenultimate level - i<level-1 - (height-2)
                print("Nivel", i, "-", level)
                for lvl in level:
                    node = self.getNode(root, int(lvl[0])) #get the node by the for
                    if node: #node exit's
                        if not(node.hasAllChilds()): #the node doesn't have all childs
                            completeBool = False #boolean false (not complete tree)"""
            i += 1 #identify the level
        if(completeBool):
            print("IT IS A COMPLETE TREE")
        else:
            print("IT IS NOT A COMPLETE TREE")
        return completeBool
                        
    def fullTree(self, root):
        fullBool = True #boolean of the method
        if root == None: #root doesnt exist
            return [] #exit of the method
        levels = self.getNodesByLevel(root) #get the array of nodes by levels
        i = 0
        for level in levels: #walk into levels array
            if(i < len(levels)-2):#goes to the antepenultimate level - i<level-1 - (height-2)
                print("Nivel", i, "-", level)
                for lvl in level:
                    node = self.getNode(root, int(lvl[0])) #get the node by the for
                    if node: #node exit's
                        if not(node.hasAllChilds()): #the node doesn't have all childs
                            fullBool = False #boolean false (not complete tree)"""
            i += 1 #identify the level
        if(fullBool):
            print("IT IS A COMPLETE TREE")
        else:
            print("IT IS NOT A COMPLETE TREE")
        return fullBool

    #Pre-order 
    def preOrder(self, root):
        print(root.name, root.id)
        if(root.hasLeftChild()):
            self.preOrder(root.leftChild)
        if(root.hasMiddleChild()):
            self.preOrder(root.middleChild)
        if(root.hasRightChild()):
            self.preOrder(root.rightChild)

    #In-Orden
    def inOrder(self, root):
        if(root.hasLeftChild()):
            self.inOrder(root.leftChild)
        if(root.hasMiddleChild()):
            self.inOrder(root.middleChild)
        print(root.name, root.id)
        if(root.hasRightChild()):
            self.inOrder(root.rightChild)

    #pos-Orden
    def posOrder(self, root):
        if(root.hasLeftChild()):
            self.posOrder(root.leftChild)
        if(root.hasMiddleChild()):
            self.posOrder(root.middleChild)
        if(root.hasRightChild()):
            self.posOrder(root.rightChild)
        print(root.name, root.id)


        #Nodes by level
    def levelOrder(self, root):
        if root == None:#If root don't exist
            return []#Return list empty
        res = [] #Create new list empty
        nodes = [root] #Create new list with element root
        while nodes:# while nodes is not emptu
            res.append([(node.id, node.name) for node in nodes])#Add node.id and node.name to list res
            next_nodes = [] #Create new list empty
            for node in nodes:#Catch nodes in nodes list
                if node.hasLeftChild():#If left child exist
                    next_nodes.append(node.leftChild)
                if node.hasMiddleChild():#If middle child exist
                    next_nodes.append(node.middleChild)
                if node.hasRightChild():#If right child exist
                    next_nodes.append(node.rightChild)
            nodes = next_nodes
        return res #Return res list of the travel by width

        #Number of nodes by Level
    def numChilds(self, root):
        res = self.levelOrder(root)
        nc = []
        for x in res:
            nc.append(len(x))

        return nc

        #Sum of totality by nodes
    def sumChilds(self, root):
        suma = 0
        nc = self.numChilds(root)
        for i in nc:
            suma = suma + i
        return suma

    def getNumsChilds(self,nodo):
        i = 0
        if(nodo.hasLeftChild()):
            i += 1
        if(nodo.hasMiddleChild()):
            i += 1
        if(nodo.hasRightChild()):
            i += 1
        return i

    def addNewNode(self, id, name, party, fatherkey):
        self.addNode(id, name, party, fatherkey)

    def getNodesByLevel(self, root):
        if(self.arrayNodesLevel):
            return self.arrayNodesLevel
        else:
            arrayNodesLevel = self.levelOrder(root)
            return arrayNodesLevel

    def levels(self, root):
        path = self.longerPath(root)
        for i in range(len(path)):
            x = i + 1
        print(x)
    
    def height(self, root):
        path = self.longerPath(root)
        for i in range(len(path)):
            x = i + 1
        print(x)

    
    def sendMessage(self, sml, currentNode, messageNode):
        name = self.getNode(self.root, currentNode).name
        ide = self.getNode(self.root, currentNode).id
        pNode = self.getNode(self.root, currentNode).parentNode
        completPath = self._paths(self.root, self.arrayPaths, self.paths) #get array of paths
        sml.append(str(ide))
        if (self.getNode(self.root, currentNode).hasParentNode()):
            self.sendMessage(sml ,self.getNode(self.root, currentNode).parentNode.id, messageNode)
        for i in completPath:
            if(i[len(i)-1] == str(messageNode)):
                iq = i
        sml.append(im)
        print(sml)
        return sml












    

    