from herramientas import *
class pesadas(herramientas):
    __tip_maqui:str
    __peso:int
    def __init__(self, marc, mode, an, tipo, pot, capa, tari, canti, tipomaqui, peso):
        super().__init__(marc, mode, an, tipo, pot, capa, tari, canti)
        self.__tip_maqui=tipomaqui
        self.__peso=int(peso)
        
    
    def getTarifaAlquiler(self):
        if self.__peso<=10:
            return super().gettarifa()*super().getDias()
        if self.__peso>10:
            valor = super().gettarifa()*super().getDias()
            return valor*1.20
    
    def __str__(self):
        return super().getMarca() + " " + super().getModelo() + ". Fabricado en: " + super().getAnio() + "; combustible: " + super().getCombustible() + "; potencia: "+ self.getPotencia() + "; y capacidad de: "  + super().getCapacidad() +". Con una tarfia de alquiler de:  $" + f"{self.getTarifaAlquiler():0.2f}"