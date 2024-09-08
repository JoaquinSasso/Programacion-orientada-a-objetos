class materialRefractario:
   __material : int
   __caracterisitcas: str
   __cantUtilizada: float
   __costoAdicional: float
   
   
   def __init__(self, id, caract, cant, costo):
      self.__material = int(id)
      self.__caracterisitcas = caract
      self.__cantUtilizada = float(cant)
      self.__costoAdicional = float(costo)