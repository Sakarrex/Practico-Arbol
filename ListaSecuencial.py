
import numpy as np

class ListaSecuencial:
    __arreglo = None
    __actualVacio = None

    def __init__(self,tamanio) -> None:
        self.__arreglo = np.empty(tamanio,dtype=int)
        self.__actualVacio = 0
    
    def lleno(self):
        return self.__actualVacio == len(self.__arreglo)
    
    def vacio(self):
        return self.__actualVacio == 0
    
    def Recuperar(self,posicion):

        if posicion < 0 or posicion >= self.__actualVacio:
            raise IndexError
        
        return self.__arreglo[posicion]
    
    def Insertar(self,elemento,posicion):
        if self.lleno():
            print("Lista llena")
        elif posicion-1 > self.__actualVacio:
            print("Posicion no valida")
        elif posicion-1 == self.__actualVacio:
            self.__arreglo[self.__actualVacio] = elemento
            self.__actualVacio += 1
        elif posicion-1 < self.__actualVacio:
            for i in range(self.__actualVacio,posicion-1,-1):
                self.__arreglo[i] = self.__arreglo[i-1]
            self.__arreglo[posicion-1] = elemento
            self.__actualVacio +=1
    
    def Suprimir(self,posicion):
        if self.vacio():
            print("No se puede suprimir lista vacia")
        elif posicion -1 > self.__actualVacio:
            print("Posicion no valida")
        elif posicion-1 == self.__actualVacio-1:
            self.__actualVacio -= 1
        elif posicion-1 < self.__actualVacio-1:
            for i in range(posicion-1,self.__actualVacio-1):
                self.__arreglo[i] = self.__arreglo[i+1]
            self.__actualVacio-=1
    
    def Buscar(self,elemento):
        pos = -1
        i = 0 
        while i < self.__actualVacio and pos == -1:
            if self.Recuperar(i) == elemento:
                pos = i
            i+=1
        if pos == -1:
            print("Elemento no encontrado")
        else:
            print("Elemento encontrado")
        
    def Recorrer(self):
        for i in range(self.__actualVacio):
            print(self.Recuperar(i))

    def Primer_Elemento(self):
        if not self.vacio():
            return self.__arreglo[0]
        else:
            raise ValueError
        
    def Ultimo_Elemento(self):
        if not self.vacio():
            return self.__arreglo[self.__actualVacio-1]
        else:
            raise ValueError
    
    def getAnterior(self,posicion):
        if not self.vacio():
            if posicion-1 <= self.__actualVacio-1 and posicion > 1:
                return self.__arreglo[posicion-2]
            else:
                raise IndexError
        else:
            raise ValueError
    
    def getSiguiente(self,posicion):
        if not self.vacio():
            if posicion-1 <= self.__actualVacio-2 and posicion > 0:
                return self.__arreglo[posicion]
            else:
                raise IndexError
        else:
            raise ValueError
    

