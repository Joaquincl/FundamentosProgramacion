##12.- Pide al usuario dos pares de números x1,y2 y x2,y2 
## que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos

coorx1= f"Ingresa la primera coordenada de X"
input(coorx1)
coorx2= f"Ingresa la segunda coordenada de X"
input(coorx2)
coory1= f"Ingresa primera coordenada de Y"
input(coory1)
coory2= f"Ingresa la segunda cordenada de Y"
input(coory2)

##la distancia entre ellos es la diferencia entre las coordenadas que no comparten
coordenadax = (coorx1 - coory1)
coordenaday = (coorx2 - coory2)

f"La distancia en la que te encuentras es de: ({coordenadax} X) , ({coordenaday} Y)"
