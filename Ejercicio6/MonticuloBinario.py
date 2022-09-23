from unicodedata import name
import numpy as np
import math
class MonticuloBinario:
    __arreglo = None
    
    def __init__(self,tamanio) -> None:
        self.__arreglo = np.empty(tamanio+1,dtype= int)
        self.__arreglo [0] = 0
    
    def Insertar(self,valor):
        self.__arreglo[self.__arreglo[0]+1] = valor
        
        padre = math.floor((self.__arreglo[0]+1)/2)
        while self.__arreglo[padre] > valor:
            padre = math.floor(padre/2)
            
        
        for j in range(self.__arreglo[0]+1,padre,-1):
            self.__arreglo[j] = self.__arreglo[j-1]
        
        self.__arreglo[padre] = valor
        self.__arreglo[0] +=1
    
    def Mostrar(self):
        for i in range(1,self.__arreglo[0]+1):
            print(self.__arreglo[i])
    

