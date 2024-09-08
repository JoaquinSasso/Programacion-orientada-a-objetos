class cliente:
    __nombre:str
    __apellido:str
    __dni:str
    __numtarj:str
    __saldoanterior:str
    def __init__(self,nombre,apellido,dni,numtarj,saldoanterior):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__numtarj=numtarj
        self.__saldoanterior=saldoanterior
    def getdni(self):
        return self.__dni
    def getnumtarj(self):
        return self.__numtarj
    def getsaldo(self):
        return self.__saldoanterior
    def setsaldo(self,saldo):
        self.__saldoanterior=saldo
    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    
