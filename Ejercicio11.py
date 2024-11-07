# Actividad 11 Pide al usuario dos números y muestra la "distancia" entre ellos 
##(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num1 = print("Ingresa el primer numero: ")
num1 = input(num1)
num2= print("Ingresa el segundo numero: ")
num2 = input(num2)
valorabsoluto = (num1- num2)

if valorabsoluto >= 0:
    print("La distancia entre los dos numeros es: ", valorabsoluto)
else:
    print("La distancia es negativa, Ingesa otros valores")
 
