from abc import ABC,abstractmethod
class herramientas(ABC):
    __marca:str
    __model:str
    __anio_fab:str
    __tip_comb:str
    __pote:str
    __cap_carg:int
    __tarif_alq:float
    __cant_dias:int
    def __init__(self,marc,mode,an,tipo,pot,capa,tari,canti):
        self.__marca=marc
        self.__model=mode
        self.__anio_fab=an
        self.__tip_comb=tipo
        self.__pote=pot
        self.__cap_carg= capa
        self.__tarif_alq=float(tari)
        self.__cant_dias=int(canti)
    
    
    @abstractmethod
    def getTarifaAlquiler(self):
        return self.__tarif_alq
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__model
    
    def getAnio(self):
        return self.__anio_fab
    
    def getCombustible(self):
        return self.__tip_comb
    
    def getCapacidad(self):
        return self.__cap_carg
    
    def getPotencia(self):
        return self.__pote
    
    def getDias(self):
        return self.__cant_dias
    
    def gettarifa(self):
        return self.__tarif_alq
    
    @abstractmethod
    def __str__(self):
        pass