from ast import Return
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

            
    def Suprimir(self,valor):
        if self.__raiz == None:
            print("Arbol vacio")
        else:
            NodoBorrar = self.Buscar(self.__raiz,valor)
            if NodoBorrar != None:
                if NodoBorrar.getValor() == valor:
                    grado = self.getGrado(NodoBorrar)
                    Padre = self.getPadre(self.__raiz,NodoBorrar.getValor())

                    if grado == 0:
                        if Padre == None:
                            self.__raiz = None
                        else:
                            if Padre.getIzquierdo()!= None and Padre.getIzquierdo().getValor() == valor:
                                Padre.setIzquierdo(None)
                            else:
                                Padre.setDerecho(None)
                            
                    elif grado == 1:
                        if Padre != None:
                            
                            if Padre.getValor() > NodoBorrar.getValor():
                                if NodoBorrar.getizquerido()!= None:
                                    Padre.setIzquierdo(NodoBorrar.getIzquierdo()) 
                                else:
                                    Padre.setIzquierdo(NodoBorrar.getDerecho()) 
                                
                            else:
                                if NodoBorrar.getizquerido()!= None:
                                    Padre.setDerecho(NodoBorrar.getIzquierdo()) 
                                else:
                                    Padre.setDerecho(NodoBorrar.getDerecho()) 
                                
                        else:
                            if self.__raiz.getIzquierdo()!= None:
                                self.__raiz = self.__raiz.getIzquierdo()
                            else:
                                self.__raiz = self.__raiz.getDerecho()

                        
                    elif grado == 2:
                        
                        NodoInfimo = self.getMenorMayores(NodoBorrar.getDerecho())
                        gradoInfimo = self.getGrado(NodoInfimo)
                        PadreInfimo = self.getPadre(self.__raiz,NodoInfimo.getValor())
                        if gradoInfimo == 1:
                            
                            print("Padre Infimo: " + str(PadreInfimo.getValor()))
                            if PadreInfimo.getIzquierdo() != None and PadreInfimo.getIzquierdo().getValor() == NodoInfimo.getValor():
                                PadreInfimo.setIzquierdo(NodoInfimo.getDerecho())
                            else:
                                PadreInfimo.setDerecho(NodoInfimo.getDerecho())
                            
                        elif gradoInfimo == 0:
                            if PadreInfimo.getIzquierdo() != None and PadreInfimo.getIzquierdo().getValor() == NodoInfimo.getValor():
                                PadreInfimo.setIzquierdo(None)
                            else:
                                PadreInfimo.setDerecho(None)


                        NodoBorrar.setValor(NodoInfimo.getValor())
                            
 
        
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
    
    def getMenorMayores(self,NodoActual):
            if NodoActual.getIzquierdo() != None:
                return self.getMenorMayores(NodoActual.getIzquierdo())
            else:
                return NodoActual
        

    def getPadre(self,NodoActual,valor):
        if self.__raiz != None and self.__raiz.getValor() == valor:
            return None
        else:
            if NodoActual.getIzquierdo() != None and NodoActual.getIzquierdo().getValor() == valor:
                return NodoActual
            elif NodoActual.getDerecho() != None and NodoActual.getDerecho().getValor() == valor:
                return NodoActual
            elif valor < NodoActual.getValor():
                return self.getPadre(NodoActual.getIzquierdo(),valor)
            elif valor > NodoActual.getValor():
                return self.getPadre(NodoActual.getDerecho(),valor)

    def Buscar(self,nodoActual,valor):
        if nodoActual == None:
            return None
        elif nodoActual.getValor() == valor:
            return nodoActual
        elif valor < nodoActual.getValor():
            return self.Buscar(nodoActual.getIzquierdo(),valor)
        else:
            return self.Buscar(nodoActual.getDerecho(),valor)
        
            
    def getFrontera(self,NodoActual):
        if NodoActual != None:
            if self.getGrado(NodoActual) == 0:
                print(NodoActual.getValor())
            self.getFrontera(NodoActual.getIzquierdo())
            self.getFrontera(NodoActual.getDerecho())
    
    def esHijo(self,ValorPadre,ValorHijo):
        Padre = self.Buscar(self.__raiz,ValorPadre)
        if Padre != None:
            if ValorHijo < ValorPadre:
                return Padre.getIzquierdo().getValor() == ValorHijo
            else:
                return Padre.getDerecho().getValor() == ValorHijo
        
    def getCamino(self,ValorInicio,ValorFin):
        NodoInicio = self.Buscar(self.__raiz,ValorInicio)
        if NodoInicio != None:
            NodoFin = self.Buscar(NodoInicio,ValorFin)
            if NodoFin != None:
                print("Existe Camino")
            else:
                print("No existe el camino")
        else:
            print("Nodo Incial no encontrado")
            
    def nivelNodo(self,valor):
        aux = self.__raiz
        Nivel = 0
        while aux != None:
            if aux.getValor() == valor:
                aux = None
            elif valor < aux.getValor():
                aux = aux.getIzquierdo()
            else:
                aux = aux.getDerecho()
            Nivel +=1
        return Nivel
    
    def CantoNodos(self,SubArbol):
        if self.__raiz == None:
            return 0
        elif SubArbol == None:
            return 0
        else:
            return 1 + self.CantoNodos(SubArbol.getIzquierdo()) + self.CantoNodos(SubArbol.getDerecho())

    def getAlturaArbol(self,subArbol,max = 1):
        if subArbol != None:
            nivel = self.nivelNodo(subArbol.getValor())
            if max < nivel:
                max = nivel 
            max = self.getAlturaArbol(subArbol.getIzquierdo(),max)
            max = self.getAlturaArbol(subArbol.getDerecho(),max)
        return max
        
    def getSucesores(self,valor):
        Nodo = self.Buscar(self.__raiz,valor)
        if Nodo != None:
            self.InOrden(Nodo.getIzquierdo())
            self.InOrden(Nodo.getDerecho())
        
    