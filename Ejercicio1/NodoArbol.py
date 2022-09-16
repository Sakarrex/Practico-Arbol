class NodoArbol:
    __valor = 0
    __izquierdo = None
    __derecho = None

    def __init__(self,valor) -> None:
        self.__valor = valor
        self.__izquierdo = None
        self.__derecho = None
    
    def setIzquierdo(self,Izquierdo):
        self.__izquierdo = Izquierdo
    
    def setDerecho(self,Derecho):
        self.__derecho = Derecho
    
    def setValor(self,valor):
        self.__valor = valor
    
    def getIzquierdo(self):
        return self.__izquierdo
    
    def getDerecho(self):
        return self.__derecho
    
    def getValor(self):
        return self.__valor
    
