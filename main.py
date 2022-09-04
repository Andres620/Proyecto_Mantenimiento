import json
from TST.TernarySearchTree import TST

myTree = TST()
#Load the file and show it
def cargarDatos(ruta):
    with open(ruta) as contenido:
        estruc = json.load(contenido)
        buscarHijos(estruc)
                    
def buscarHijos(estr):
    for pers in estr.get('people'):
        print(pers.get('id'), pers.get('name'))
        myTree.addNode(pers.get('id'), pers.get('name'), pers.get('party'), 0) #NUEVA
        _buscarHijos(pers)
        
def _buscarHijos(padre):
    for pad in padre.get('childrens'):
        print(padre.get('id'),".",pad.get('id'), pad.get('name'))
        myTree.addNode(pad.get('id'), pad.get('name'), pad.get('party'),padre.get('id')) #NUEVA
        #hasChilds(pad)
        hijos = str(pad.get('childrens'))
        if(hijos != "[]"):
            _buscarHijos(pad)

def update():
    
    print("\n")
    print ("----Level Order----")
    myTree.levelOrder(myTree.root)


    print("\n\n")
    print ("----Preorder----")
    myTree.preOrder(myTree.root)

    print("\n\n")
    print ("----Inorder----")
    myTree.inOrder(myTree.root)


    print("\n\n")
    print ("----Posorde")
    myTree.posOrder(myTree.root)

    print("\n")
    print ("----Longer Path----")
    myTree.longerPath(myTree.root)

    print("\n")
    print ("----Complete Tree----")
    myTree.completeTree(myTree.root)
    
    print("\n")
    print ("----Full Tree----")
    myTree.fullTree(myTree.root)

ruta = "JSON_Information/formatJSON.json"
cargarDatos(ruta)
update()