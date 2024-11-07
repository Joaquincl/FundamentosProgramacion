C1 = float(input('Ingresa la calificación 1: '))
C2 = float(input('Ingresa la calificación 2: '))
C3 = float(input('Ingresa la calificación 3: '))
EF = float(input('Ingresa la calificación del examen final: '))
TF = float(input('Ingresa la calificación trabajo final: '))
PC = (C1+C2+C3)/3
CF = (PC*0.55)+(EF*0.30)+(TF*0.15)
print("La calificación final es de:",CF)
