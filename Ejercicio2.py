"""
Programa que calcule el área y el perimetro 
de un rectangulo a partir de su base y su altura
Entradas:
     basse: integer
     altura: integer
Salidas:
    perimetro: integer
    área: integer     
Analisis:
    Se requiere clacular con las frormulas para
    área y perimetro
"""
# input siempre regresa un string
# para tratarlo como otro dato se debe convertir
base = input("Escribe la base del rectángulo: ")
base = int(base)
altura = input("Escribe la altura del rectángulo: ")
altura = int(altura)
area = base * altura
perimetro = (base + altura) *  2
print("El area del rectangulo es ", area)
print("El perimetro del rectangulo es ", perimetro)

