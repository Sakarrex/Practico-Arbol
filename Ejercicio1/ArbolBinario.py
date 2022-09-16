from NodoArbol import NodoArbol

class ArbolBinario:
    __raiz = None

    def __init__(self) -> None:
        self.__raiz = None
    
    def Insertar(self,SubArbol,valor):
        if self.__raiz == None:
            NuevoNodo = NodoArbol(valor)
            self.__raiz = NuevoNodo
        elif SubArbol != None:
            if SubArbol.getValor() == valor:
                print("Valor ya ingresado")
            elif valor < SubArbol.getValor():
                if SubArbol.getIzquierdo() == None:
                    NuevoNodo = NodoArbol(valor)
                    SubArbol.setIzquierdo(NuevoNodo)
                else:
                    self.Insertar(SubArbol.getIzquierdo(),valor)
            elif valor > SubArbol.getValor():
                if SubArbol.getDerecho() == None:
                    NuevoNodo = NodoArbol(valor)
                    SubArbol.setDerecho(NuevoNodo)
                else:
                    self.Insertar(SubArbol.getDerecho(),valor)

            
    def Suprimir(self,NodoActual,valor):
        if self.__raiz == None:
            print("Arbol vacio")
        else:
            if NodoActual.getValor() > valor:
                grado = self.getGrado(NodoActual)
                if grado == 0:
                    NodoActual = None
                elif grado == 1:
                    if NodoActual.getIzquierdo() != None:
                        NodoActual.setValor(NodoActual.getIzquierdo().getValor())
                        NodoActual.setIzquierdo(None)
                    elif NodoActual.getDerecho() != None:
                        NodoActual.setValor(NodoActual.getDerecho().getValor())
                        NodoActual.setDerecho(None)
                elif grado == 2:
                    valor = self.getMenorMayores(self.__raiz)
                    NodoActual.setValor(valor)
            else:
                if NodoActual.getValor() > valor:
                    self.Suprimir(NodoActual.getIzquierdo(),valor)
                elif NodoActual.getValor() < valor:
                    self.Suprimir(NodoActual.getDerecho(),valor)

                    
                
            
        
    def InOrden(self,SubArbol):
        if SubArbol != None:
            self.InOrden(SubArbol.getIzquierdo())
            print(SubArbol.getValor())
            self.InOrden(SubArbol.getDerecho())
    
    def PreOrden(self,SubArbol):
        if SubArbol != None:
            print(SubArbol.getValor())
            self.PreOrden(SubArbol.getIzquierdo())
            self.PreOrden(SubArbol.getDerecho())

    def PostOrden(self,SubArbol):
        if SubArbol != None:
            self.PostOrden(SubArbol.getIzquierdo())
            self.PostOrden(SubArbol.getDerecho())
            print(SubArbol.getValor())

    def getRaiz(self):
        return self.__raiz
    
    def getGrado(self,Nodo):
        grado = -1
        if Nodo.getDerecho() == None and Nodo.getIzquierdo() == None:
            grado = 0
        elif (Nodo.getDerecho() == None and Nodo.getIzquierdo() != None) or (Nodo.getDerecho() != None and Nodo.getIzquierdo() == None):
            grado = 1
        elif Nodo.getDerecho() != None and Nodo.getIzquierdo() != None:
            grado = 2
        return grado
    
    def getMenorMayores(self,NodoActual,nivelActual=1):
        if nivelActual == 1:
            self.getMenorMayores(NodoActual.getDerecho(),nivelActual+1)
        elif nivelActual >= 2:
            if NodoActual.getIzquierdo() != None:
                self.getMenorMayores(NodoActual.getIzquierdo(),nivelActual+1)
            else:
                valor = NodoActual.getValor()
                NodoActual = None
                return valor
        

        

        
