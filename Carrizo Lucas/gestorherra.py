from electricas import electricas
from pesadas import pesadas
from nodo import *
import csv
class gestorherra:
    __cab:nodo
    __actu:nodo
    __indice:int
    __tope:int
    def __init__(self,cab=None,actu=None,indi=0,tope=0):
        self.__cab=cab
        self.__actu=actu
        self.__indice=indi
        self.__tope=tope
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actu=self.__cab
            self.__indice=0
            raise StopIteration
        else:
            dat=self.__actu.getdat()
            self.__indice+=1
            self.__actu=self.__actu.getsig()
            return dat
    
    def agreg(self,obje):
        nuevo=nodo(obje)
        if self.__cab == None:
            self.__cab = nuevo
            self.__actu = self.__cab
            self.__tope += 1
        else:
            nodau=self.__cab
            while nodau.getsig() != None:
                nodau=nodau.getsig()
            if nodau.getsig() == None:
                nodau.setSig(nuevo)
                self.__tope += 1
    
    def carga(self):
        a=open('equipos.csv')
        re=csv.reader(a, delimiter=';')
        saltar = False
        for fil in re:
            if saltar == False:
                saltar = True
            else:
                if fil[0]== 'M':
                    herramienta = pesadas(fil[1],fil[2],fil[3],fil[4],fil[5],fil[6],fil[7],fil[8],fil[9],fil[10])
                elif fil[0] == 'E':
                    herramienta = electricas(fil[1],fil[2],fil[3],fil[4],fil[5],fil[6],fil[7],fil[8],fil[9])
                self.agreg(herramienta)
    
    
    def buscarIndice(self, ind):
        self.__actu = 0
        actual = self.__cab
        while self.__actu != ind and self.__actu < self.__tope:
            actual = actual.getsig()
            self.__actu += 1
        self.__actu = 0
        return actual.getdat()
    
    
    def inciso1(self,ind):
        if ind >= self.__tope:
            raise IndexError
        else:
            equipo = self.buscarIndice(ind)
            if isinstance(equipo, pesadas):
                print('Es una herramienta pesada!')
            elif isinstance(equipo, electricas):
                print('Es una herramienta electrica!')
    
    def inciso2(self, anio):
        cant=0
        for equipo in self:
            if isinstance(equipo, electricas):
                if equipo.getAnio() == anio:
                    cant += 1
        print(f"Hay {cant} maquinas fabricadas este año")
    
    def inciso3(self, capa):
        cont=0
        for equipo in self:
            if isinstance(equipo,pesadas):
                if int(equipo.getCapacidad()) <= capa:
                    cont+=1
        print(f'Las herramientas pesadas cuya capacidad es menor a {capa} es {cont}')
    
    def inciso4(self):
        for equipo in self:
            print(equipo)
    