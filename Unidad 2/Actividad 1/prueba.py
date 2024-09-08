def prueba():
   cuil = "20-45263619-1"
   numeros = []
   for caracter in cuil:
         if caracter != '-':
            numeros.append(int(caracter))
   print(numeros)
   
prueba()