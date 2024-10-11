'''
Ejercicio 3 
  Programa que calcula la hipotenusa a partir de los dos catetos ç
Entradas:
   CatetoA: int - a
   CatetoB: int - b
Salidas:
   hipotenusa: float - c

Análisis:
   Se utiliza el teorema de Pitágoras
'''
a = input ("Escribe el valor de cateto A: ")
a = int (a)
b = input ("Escribe el valor del cateto B: ")
b = int (b)
c = (a * a + b * b) ** (1 / 2)
print("El valor de a hipotenusa: ", c)