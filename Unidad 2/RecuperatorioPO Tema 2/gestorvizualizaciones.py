import csv
from clasevizualizacion import visualizacion
class gestorvizualizacion:
    __lista:list
    def __init__(self):
        self.__lista=[]
        archivo=open("Visualizaciones.csv")
        reader=csv.reader(archivo, delimiter=";")
        bandera=False
        for fila in reader:
            if bandera==False:
                bandera=True
            else:
                idmiembro=int(fila[0])
                idpelicula=fila[1]
                fecha=fila[2]
                hora=fila[3]
                min=int(fila[4])
                vizualizaciones=visualizacion(idmiembro,idpelicula,fecha,min,hora)
                self.__lista.append(vizualizaciones)
        archivo.close()
        


    def contarMinutosUsuario(self, idM):
        total = 0
        for visualizacion in self.__lista:
            if visualizacion.getidmiembro() == idM:
                total += visualizacion.getmin()
        return total
    
    
    def visualizacionesSimultaneas(self, gestorM):
        repetidos = []
        for i in range(len(self.__lista)):
            for j in range(len(self.__lista)):
                if ((i != j )and (self.__lista[i] == self.__lista[j]) and(i not in repetidos)):
                    repetidos.append(j)
                    gestorM.mostrarDatos(self.__lista[i].getidmiembro())