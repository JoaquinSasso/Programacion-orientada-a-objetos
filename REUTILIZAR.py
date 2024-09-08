"""
def menu():
    GC=gestorC()
    GR=gestorR()
    GC.agregarcabañas()
    GR.cargar()
    k=-1
    while(k!=0):
        opcion=int(input("ingresar una opcion:\n1.Mostrar Cabañas Disponibles\n2. \n3.salir\n"))
        if opcion==3:
            k=0
        elif (opcion==1):
            GC.muestracabañas(GR)

        #elif(opcion==2):
if __name__=='__main__':
    menu()
-----------------------------------------------------------------------
def __init__(self):
        self.__cant=0
        self.__dimension=0
        self.__incremento=5
        self.__listacabañas= np.empty([0],dtype=cabaña)
            
    if self.__cant==self.__dimension:
        self.__dimension+=self.__incremento
        self.__listacabañas.resize(self.__dimension)    
--------------------------------------------------------------------------------------   
    def guardarcuentas(self):
        archivo=open("cuentasActualizadas.csv","w", newline="")
        writer=csv.writer(archivo,delimiter=";")
        writer.writerow(["Apellido","Nombre","dni","telefono","saldo","cvu",])
        for i in range (len(self.__cuentas)):
            ap=self.__cuentas[i].getapellido()
            nomb=self.__cuentas[i].getnombre()
            dni=self.__cuentas[i].getdni()
            tel=str(self.__cuentas[i].gettelefono())
            saldo=str(self.__cuentas[i].getsaldo())
            cvu=str(self.__cuentas[i].getcvu())
            array=[ap,nomb,dni,tel,saldo,cvu]
            writer.writerow(array)
        archivo.close()
    --------------------------------------------------------
    def __iter__(self):
      return self
   
   def __next__(self):
      if self.__indice == self.__tope:
         self.__actual = self.__comienzo
         self.__indice = 0
         raise StopIteration
      else:
         self.__indice += 1
         dato = self.__actual.datos()
         self.__actual = self.__actual.sig()
         return dato
         
    
   ---------------------------------------------------------------------------------- 
    
    
    class nodo:
   __sig : object
   __datos : object
   
   def __init__(self, sig, datos):
      self.__sig = sig
      self.__datos = datos
      
   
   def datos(self):
      return self.__datos
   
   def sig(self):
      return self.__sig
   
   def setSig(self, nodo):
      self.__sig = nodo
    -----------------------------------------------------
    def insertarFinal(self,objeto)
    aux=self.__comienzo
    while aux.getsiguiente()!=None:
        anterior=aux
        aux=aux.getsiguiente()
    anterio=aux
    unnodo=nodo(objeto)
    unnodo.setsiguiente(aux.getsiguiente())
    anterior.setsiguiente(unnodo)
    ---------------------------------------------
import json
from pathlib import Path
class objetEncoder:
   def cargarJSON(self):
         with Path("personal.json").open("r", encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close
         print("Se leyo el archivo")
         return diccionario

   def decodificarDiccionario(self, d):
         if "clase" not in d:
            return d
         else:
            class_name = d["clase"]
            class_ = eval(class_name)
            if class_name == "lista":
               agentes = d["agentes"]
               gestor = lista()
               for i in range(len(agentes)):
                  dAgente = agentes[i]
                  class_name = dAgente.pop("clase")
                  class_=eval(class_name)
                  atributos = dAgente["atributos"]
                  unAgente = class_(**atributos)
                  gestor.agregarElemento(unAgente)
            return gestor








         def agentesToJSON(self): #llama tojson de las clases
         arreglo = []
         for agente in self:
            arreglo.append(agente.toJSON())
         return arreglo
      
      
      def toJSON(self):  #los dos TO van juntos
         diccionario = dict(
            clase = __class__.__name__,
            agentes = self.agentesToJSON()
         )
         return diccionario
         
         def toJSON(self): #en las clases
         diccionario = dict(
         clase = __class__.__name__, 
         atributos = dict(
            cuil = self.__cuil,
            nombre = self.getNombre(),
            apellido = self.getApellido(),
            sueldoBasico = self.getSueldoBasico(),
            antiguedad = self.getAntiguedad()
         )
         )
         return diccionario
      
      
         
      def guardarJSON(self, diccionario):
         with Path("personal.json").open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
         print("Se guardo el archivo")
    ------------------------------------------------------------------------------------
from zope.interface import Interface

class InterfacePolicia(Interface):
   
   def crearPersona(self):
      pass

   def crearAntecedente(self):
      pass


from moduloInterfaz import InterfacePolicia
from zope.interface import implementer

@implementer(InterfacePolicia)
-----------------------------------------------------------------------------------------
from GestorPersona import GestorPer
from ClaseAntecedente import antecedente
from ClasePersona import persona
import unittest
class testing(unittest.TestCase):
    __GP: GestorPer
    def setUp(self):
        self.__GP=GestorPer()
        unapersona=persona("Lucas","Valido","27/08/2004","45885130",None,None,None,None)
        self.__GP.cargaPersona(unapersona)
        unapersona=persona("German","Reta","27/08/2003","45885131",None,None,None,None)
        self.__GP.cargaPersona(unapersona)
        unantecedente=antecedente("20/07/1999","Mucha Facha",9999.3,"No Cumplida",2525)
        self.__GP.agregarAntecedente("45885131",unantecedente)
    def test_buscar(self):
        unapersona=persona("Lucas","Valido","27/08/2004","45885130",None,None,None,None)
        self.assertEqual(unapersona,self.__GP.buscarPersona("45885130"))
if __name__ == '__main__':
    unittest.main()
    """