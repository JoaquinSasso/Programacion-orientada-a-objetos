import csv
import  numpy as np
from clasemiembro import miembro
from gestorvizualizaciones import gestorvizualizacion
class gestormiembros:
    __lista:np.ndarray
    __dimension:int
    __incremento:int
    __cantidad:int
    def __init__(self,):
        self.__lista=np.empty(0,dtype=miembro)
        self.__dimension=0
        self.__incremento=1
        self.__cantidad=0
        archivo=open("Miembros.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            else:
                idmiembro=int(fila[0])
                nya=fila[1]
                correo=fila[2]
                miembros=miembro(idmiembro,nya,correo)
                if self.__dimension==self.__cantidad:
                    self.__dimension+=self.__incremento
                    self.__lista.resize(self.__dimension)
                self.__lista[self.__cantidad]=miembros
                self.__cantidad+=1
        archivo.close()
        
    
    def buscarMiembro(self, correo):
        i = 0
        while((i < self.__cantidad) and (self.__lista[i].getcorreo() != correo)):
            i += 1
        if i >= self.__cantidad:
            i = -1
        return i
    
    def minutosVisualizados(self, gestorV: gestorvizualizacion, correo):
        i = self.buscarMiembro(correo)
        idM = self.__lista[i].getidmiembro()
        minutos = gestorV.contarMinutosUsuario(idM)
        print(f"El usuario: {self.__lista[i].getnya()} tiene {minutos} minutos visualizados")
    
    
    def mostrarDatos(self, idM):
        i = 0
        while((i < self.__cantidad) and (self.__lista[i].getidmiembro() != idM)):
            i += 1
        if i < self.__cantidad:
            print(f"El usuario {self.__lista[i].getnya()} con correo {self.__lista[i].getcorreo()} tiene visualizaciones simultaneas")
    
        
        
