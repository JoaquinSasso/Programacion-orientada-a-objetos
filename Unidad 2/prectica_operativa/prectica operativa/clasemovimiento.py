class movimiento:
    __numtarj:str
    __fecha:str
    __descripcion:str
    __tipmov:str
    __importe:float
    def __init__(self,numtarj,fecha,descripcion,tipmov,importe):
        self.__numtarj=numtarj
        self.__fecha=fecha
        self.__descripcion=descripcion
        self.__tipmov=tipmov
        self.__importe=importe

    def gettipo(self):
        return self.__tipmov
    def getimporte(self):
        return self.__importe
    def getnumtarj(self):
        return self.__numtarj
    def getfecha(self):
        return self.__fecha
    def getdescripcion(self):
        return self.__descripcion
    
    def __lt__(self, otro):
        return self.__numtarj < otro.getnumtarj()