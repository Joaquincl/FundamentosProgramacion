## Realiza un algoritmo que lea un numero y muestre su raiz cubica y cuadrada
import math

# Leer el número ingresado por el usuario
num = float(input("Ingresa un número: "))

# Calcular la raíz cuadrada y la raíz cúbica
raiz_cuadrada = math.sqrt(num)
raiz_cubica = num ** (1/3)

# Mostrar los resultados
print(f"La raíz cuadrada de {num} es: {raiz_cuadrada:.2f}")
print(f"La raíz cúbica de {num} es: {raiz_cubica:.2f}")
