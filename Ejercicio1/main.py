
from ArbolBinario import ArbolBinario

if __name__ == "__main__":
    UnArbol = ArbolBinario()
    UnArbol.Insertar(UnArbol.getRaiz(),5)
    UnArbol.Insertar(UnArbol.getRaiz(),2)
    
    UnArbol.PreOrden(UnArbol.getRaiz())
    
    print("------------------------------")
    UnArbol.Suprimir(5)
    UnArbol.PreOrden(UnArbol.getRaiz())
    
    