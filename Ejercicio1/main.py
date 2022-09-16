
from ArbolBinario import ArbolBinario

if __name__ == "__main__":
    UnArbol = ArbolBinario()
    UnArbol.Insertar(UnArbol.getRaiz(),5)
    UnArbol.Insertar(UnArbol.getRaiz(),2)
    UnArbol.Insertar(UnArbol.getRaiz(),1)
    UnArbol.Insertar(UnArbol.getRaiz(),10)
    UnArbol.Insertar(UnArbol.getRaiz(),3)
    UnArbol.Insertar(UnArbol.getRaiz(),7)
    UnArbol.Insertar(UnArbol.getRaiz(),12)
    UnArbol.Insertar(UnArbol.getRaiz(),15)
    UnArbol.PreOrden(UnArbol.getRaiz())
    print("------------------------------")
    print(UnArbol.getMenorMayores(UnArbol.getRaiz()))