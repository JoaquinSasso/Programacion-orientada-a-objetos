import numpy as np
import csv
from clasemovimiento import movimiento

class gestormovimiento:
    __lista:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int
    def __init__(self):
        self.__lista=np.empty(0,dtype=movimiento)
        self.__dimension=0
        self.__cantidad=0
        self.__incremento=1
        archivo=open("MovimientosAbril2024.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                numtarj=fila[0]
                fecha=fila[1]
                descripcion=fila[2]
                tipmov=fila[3]
                importe=float(fila[4])
                movimientos=movimiento(numtarj,fecha,descripcion,tipmov,importe)
                if self.__dimension==self.__cantidad:
                    self.__dimension+=self.__incremento
                    self.__lista.resize(self.__dimension)
                self.__lista[self.__cantidad]=movimientos
                self.__cantidad+=1
        archivo.close()
    def modificarsaldo(self,numtarj):
        self.__lista.sort()
        i=0
        nuevoimporte = 0
        print("movimientos")
        print("fecha    descripcion                 importe     tipo ")
        while (i<len(self.__lista)):
            if self.__lista[i].getnumtarj()==numtarj:
                print(f"{self.__lista[i].getfecha()}        {self.__lista[i].getdescripcion()}        {self.__lista[i].getimporte()}    {self.__lista[i].gettipo()}")
                if self.__lista[i].gettipo()== "C":
                    nuevoimporte+= self.__lista[i].getimporte()
                if self.__lista[i].gettipo()== "P":
                    nuevoimporte-=self.__lista[i].getimporte()
            i += 1
        return nuevoimporte