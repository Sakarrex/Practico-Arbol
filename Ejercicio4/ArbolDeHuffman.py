from fileinput import close
import string
from NodoArbol import NodoArbol

class ArbolDeHuffman:
    __raiz = None

    def __init__(self) -> None:
        listaNodos = []
        archivo = open("C:\\Users\\Usuario\\Desktop\\Estructura de datos y algoritmos\\Practico-Arbol\\Ejercicio4\\texto.txt", "r")
        texto = ""
        for line in archivo:
            texto += line
        archivo.close()
        texto = texto.translate({ord(c): None for c in string.whitespace}).lower()
        for i in range(len(texto)):
            if texto[i] not in listaNodos:
                nodo = NodoArbol(texto[i],texto.count(texto[i]))
                listaNodos.append(nodo)
        listaNodos.sort()
        

        while len(listaNodos) >= 2:
            NuevoNodo = NodoArbol(listaNodos[0].getCaracter()+listaNodos[1].getCaracter(),listaNodos[0].getValor()+listaNodos[1].getValor())
            
            NuevoNodo.setIzquierdo(listaNodos[0])
            NuevoNodo.setDerecho(listaNodos[1])
            listaNodos.pop(0)
            listaNodos.pop(0)
            listaNodos.append(NuevoNodo)
            listaNodos.sort()
            
        
        self.__raiz = listaNodos[0]

    def PreOrden(self,SubArbol):
        if SubArbol != None:
            print("Caracter: {}, Frecuencia: {}".format(SubArbol.getCaracter(),SubArbol.getValor()))
            self.PreOrden(SubArbol.getIzquierdo())
            self.PreOrden(SubArbol.getDerecho())
    
    def getRaiz(self):
        return self.__raiz


    
    