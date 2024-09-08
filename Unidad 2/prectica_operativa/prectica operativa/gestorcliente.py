import csv
from clasescliente import cliente
from gestormovimiento import gestormovimiento
class gestorcliente:
    __lista:list
    def __init__(self):
        self.__lista=[]
        archivo=open("ClientesAbril2024.csv")
        reader=csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                nombre=fila[0]
                apellido=fila[1]
                dni=fila[2]
                numtarj=fila[3]
                saldoanterior=float(fila[4])
                clientes=cliente(nombre,apellido,dni,numtarj,saldoanterior)
                self.__lista.append(clientes)
        archivo.close()
    def buscar(self,dni):
        i=0
        while ((i<len(self.__lista)) and (dni!=self.__lista[i].getdni())):
            i+=1
        if i>=len(self.__lista):
            i=-1
        return i 
    def actualizar(self,dni,movimientos):
        i=self.buscar(dni)
        if i!=-1:
            print(f"el nombre del cliente es:{self.__lista[i].getnombre()} {self.__lista[i].getapellido()}")
            print(f"el numero de la tarjeta: {self.__lista[i].getnumtarj()}")
            print(f"elsaldo es:{self.__lista[i].getsaldo()}")
            numtarj=self.__lista[i].getnumtarj()
            actualizarsaldo=movimientos.modificarsaldo(numtarj)
            saldoanterior=self.__lista[i].getsaldo()
            saldoanterior+=actualizarsaldo
            self.__lista[i].setsaldo(saldoanterior)
            print(f"Nuevo importe: {saldoanterior}")