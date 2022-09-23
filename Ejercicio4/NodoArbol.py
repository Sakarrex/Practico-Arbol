import string


class NodoArbol:
    __caracter = ""
    __valor = 0
    __izquierdo = None
    __derecho = None

    def __init__(self,caracter,valor) -> None:
        self.__valor = valor
        self.__caracter = caracter
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

    def getCaracter(self):
        return self.__caracter
    
    def __eq__(self, otro):
        if type(otro) == str:
            return self.__caracter == otro

    def __str__(self) -> str:
        return "Caracter: {}, valor: {}".format(self.__caracter,self.__valor)
    
    def __gt__(self,otro):
        if type(otro) == NodoArbol:
            return otro.getValor() < self.__valor