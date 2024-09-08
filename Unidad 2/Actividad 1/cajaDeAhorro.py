class cajaDeAhorro:
   __nroCuenta : str
   __cuil: str
   __apellido: str
   __nombre: str
   __saldo: float
   def __init__(self, nro, Cuil, Apellido, Nombre, Saldo):
      self.__nroCuenta = nro
      self.__cuil = Cuil
      self.__apellido = Apellido
      self.__nombre = Nombre
      self.__saldo = Saldo
   def mostrarDatos(self):
      print(f"El numero de la cuenta es: {self.__nroCuenta} y el cuil asociado es {self.__cuil}")
      print(f"El nombre del cliente es: {self.__nombre} {self.__apellido}")
      print(f"El saldo de la cuenta es: {self.__saldo}")
   def extraer(self, importe):
      saldoRestante = self.__saldo - importe
      if saldoRestante > 0:
         self.__saldo -= importe
      return saldoRestante
   def depositar(self, importe):
      if importe > 0:
         self.__saldo += importe
         print(f"El saldo actual es de: {self.__saldo}")
      else:
         print("No se puede depositar un monto negativo")
   def validarCUIL(self):
      valido = False
      numeros = []
      resultados = [0,0,0,0,0,0,0,0,0,0]
      for caracter in self.__cuil:
         if caracter != '-':
            numeros.append(int(caracter))
      resultados[0] = numeros[0] * 5
      resultados[1] = numeros[1] * 4
      resultados[2] = numeros[2] * 3
      resultados[3] = numeros[3] * 2
      resultados[4] = numeros[4] * 7
      resultados[5] = numeros[5] * 6
      resultados[6] = numeros[6] * 5
      resultados[7] = numeros[7] * 4
      resultados[8] = numeros[8] * 3
      resultados[9] = numeros[9] * 2
      total = 0
      for i in range(len(numeros)-1):
         total += resultados[i]
      resto = total % 11
      if resto == 0:
         if numeros[10] == 0:
            print("El cuil es valido y el numero de verificacion es 0")
            valido = True
         else:
            print("El cuil no es correcto")
      elif resto == 1:
         if numeros[1] == 3:
            if numeros[10] == 9:
               print("El cuil es correcto y el numero de verificacion es 9")
               valido = True
            elif numeros[10] == 4:
               print("El cuil es correcto y el numero de verificacion es 4")
               valido = True
            else:
               print("El cuil no es correcto")
      else:
         z = 11 - resto
         if numeros[10] == z:
            print(f"El cuil es valido y el numero de verificacion es {z}")
            valido = True
         else:
            print("El cuil no es correcto")
      return valido
   