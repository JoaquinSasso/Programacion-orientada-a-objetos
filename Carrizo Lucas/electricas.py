from herramientas import herramientas
class electricas(herramientas):
    __tipo_elec:str
    def __init__(self, marc, mode, an, tipo, pot, capa, tari, canti, tipoele):
        super().__init__(marc, mode, an, tipo, pot, capa, tari, canti)
        self.__tipo_elec=tipoele
        
    
    def getTarifaAlquiler(self):
        if self.__tipo_elec == "bateria":
            valor=super().gettarifa()*super().getDias()
            return valor*1.10
        if self.__tipo_elec == "cable":
            return super().gettarifa()*super().getDias()
        
    def __str__(self):
        return super().getMarca() + " " + super().getModelo() + ". Fabricado en: " + super().getAnio() + "; potencia: "+ self.getPotencia() + " con una tarfia de alquiler de:  $" + f"{self.getTarifaAlquiler():0.2f}"
        