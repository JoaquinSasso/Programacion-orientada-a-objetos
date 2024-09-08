from ClaseMovimientos import movimiento
import csv
import numpy as np
class GestorM:
    __cant : int
    __icremento : int
    __dimension : int
    __movimientos : np.ndarray
    def __init__(self):
        self.__movimientos = np.empty([0],dtype=movimiento)
        self.__cant = 0
        self.__dimension = 0
        self.__incremento = 0
    def test(self):
        archivo=open('MovimientosAbril2024.csv')
        leer=csv.reader(archivo, delimiter=';')
        row_count = sum(1 for fila in archivo)
        self.__incremento = row_count
        bandera = False    
        for fila in leer:
            if bandera == False:
                bandera = True
            else:
                if (self.__cant==self.__dimension):
                    self.__dimension += self.__incremento
                    self.__movimientos.resize(self.__dimension)
                nro=int(fila[0])
                fecha=fila[1]
                descripcion=fila[2]
                tipo=fila[3]
                importe=float(fila[4])
                unmovimiento=movimiento(nro,fecha,descripcion,tipo,importe)
                self.__movimientos[self.__cant]=unmovimiento
                self.__cant+=1
    def ordenar(self):
        self.__movimientos.sort()
    def modificasaldo(self,nro,saldo):
        nuevosaldo=saldo
        for i in range (len(self.__movimientos)):
            if(nro==self.__movimientos[i].getnro()):
                if(self.__movimientos[i].gettipo()=='C'):
                    nuevosaldo+=self.__movimientos[i].getimporte()
                elif(self.__movimientos[i].gettipo()=='P'):
                    nuevosaldo+=self.__movimientos[i].getimporte()
            print("movimientos")
            print("fecha     descripcion     importe")
            print(f"{self.__movimientos[i].getfecha()}     {self.__movimientos[i].getdescripcion()}     {self.__movimientos[i].getimporte()}")
            print(f"saldo actualizado: {nuevosaldo}")
        return nuevosaldo
    def informar(self,GC):
        dni=input("ingresar dni\n")
        nro=GC.buscardni(dni)
        i=0
        while((i<len(self.__movimientos)) and (nro!=self.__movimientos[i].getnro())):
            i+=1
        if((i<len(self.__movimientos)) and (nro==self.__movimientos[i].getnro())):
            print("Ha realizado movimientos en el mes de abril")
        else:
            print("no ha realizado movimentos en el mes de Abril")