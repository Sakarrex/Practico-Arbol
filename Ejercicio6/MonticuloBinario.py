
import numpy as np
import math
class MonticuloBinario:
    __arreglo = None
    
    def __init__(self,tamanio) -> None:
        self.__arreglo = np.empty(int(tamanio)+1,dtype= int)
        self.__arreglo [0] = 0
    
    def Insertar(self,valor):
        self.__arreglo[self.__arreglo[0]+1] = valor
        
        
        actual = self.__arreglo[0]+1
        padre = math.floor(actual/2)

        while padre != 0 and self.__arreglo[padre] > self.__arreglo[actual] :
            aux = self.__arreglo[actual]
            self.__arreglo[actual] = self.__arreglo[padre]
            self.__arreglo[padre] = aux
            actual = padre
            padre = math.floor(actual/2)

            
        self.__arreglo[0] +=1
    
    def Eliminar_Minimo(self):
        self.__arreglo[1] = self.__arreglo[self.__arreglo[0]]
        self.__arreglo[0] -= 1

        i = 1
        band = False
        while i <= self.__arreglo[0] and band == False:

            if i*2 <= self.__arreglo[0] and self.__arreglo[i] > self.__arreglo[i*2] :
                aux = self.__arreglo[i]
                self.__arreglo[i] = self.__arreglo[i*2]
                self.__arreglo[i*2] = aux
            if (i*2)+1 <= self.__arreglo[0] and self.__arreglo[i] > self.__arreglo[(i*2)+1]:
                aux = self.__arreglo[i]
                self.__arreglo[i] = self.__arreglo[(i*2)+1]
                self.__arreglo[(i*2)+1] = aux
            else:
                band = True
            i+=1
            
                

    def Mostrar(self):
        for i in range(1,self.__arreglo[0]+1):
            print(self.__arreglo[i])
    

