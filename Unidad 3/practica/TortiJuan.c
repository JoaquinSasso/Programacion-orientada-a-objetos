#include <stdio.h>
const int N = 7;
float contarImpares(float arreglo[N])
{
   int cantidadImpares = 0;
   float totalComponentes = 0;
   for(int i = 0; i < N; i++)
   {
      if ((int)arreglo[i] % 2 == 0)
      {
         cantidadImpares = cantidadImpares + 1;
      }
      totalComponentes = totalComponentes + arreglo[i];
   }
   printf("La cantidadd de componentes impares es de: %d\n", cantidadImpares);
   return totalComponentes;
}

int main()
{
   float totalComponentes, numero;
   float arreglo[N];
   for(int i = 0; i < N; i++)
   {
      printf("Ingrese la componente %d\n", i+1);
      scanf("%f", &numero);
      arreglo[i] = numero;
   }
   totalComponentes = contarImpares(arreglo);
   printf("La suma total de las componentes del arreglo es de: %f\n", totalComponentes);
   printf("Nombre: Juan Cruz Torti Bogni\n");
   return 0;
}

/*Lote de prueba
6.54
3.93
2.78
5.01
7.61
22.22
11.49
*/