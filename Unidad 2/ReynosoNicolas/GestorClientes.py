from ClaseClientes import cliente
import csv
class GestorC:
    def __init__(self):
        self.__clientes=[]
    def agregarcliente(self, uncliente):
        self.__clientes.append(uncliente)
    def test(self):
        archivo=open('ClientesFarmaCiudad.csv')
        leer=csv.reader(archivo, delimiter=';')
        next(leer)
        for fila in leer:
            nomb=fila[0]
            ap=fila[1]
            dni=fila[2]
            nro=int(fila[3])
            saldo=float(fila[4])
            uncliente=cliente(nomb,ap,dni,nro,saldo)
            self.agregarcliente(uncliente)
            
            
    def modifsaldo(self,GM):
        dni=input("Ingresar DNI del cliente\n")
        #GM.ordenar()
        i=0
        k=len(self.__clientes)
        while((i<k)) and (dni!=self.__clientes[i].getdni()):
            i+=1
        if(i<k) and (dni==self.__clientes[i].getdni()):
            saldo=self.__clientes[i].getsaldo()
            nro=self.__clientes[i].getnro()
            print(f"Cliente: {self.__clientes[i].getapellido()} {self.__clientes[i].getnombre()}                       NRO de cuenta:{nro}")
            print(f"Saldo Anterior: {saldo}")
            saldonuevo=GM.modificasaldo(nro,saldo)
            self.__clientes[i].modifsaldo(saldonuevo)
        else:
            print("dni no encontrado")
    def buscardni(self,dni):
        i=0
        while((i<(len(self.__clientes)))) and (dni!=self.__clientes[i].getdni()):
            i+=1
        if(i<i<(len(self.__clientes))) and (dni==self.__clientes[i].getdni()):
            print(f"el cliente: {self.__clientes[i].getapellido()} {self.__clientes[i].getnombre()}")
        return self.__clientes[i].getnro()