## 8.- Un vendedor recibe un sueldo base más un 10% extra por comisión de sus 
## ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de 
## comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes 
## tomando en cuenta su sueldo base y comisiones.

sueldobase = input("Ingresa el sueldo base: ")
sueldobase= float  (sueldobase)

venta1= input("Ingresa el monto de la primera venta: ")
venta1= float (venta1)

venta2 = input("Ingresa el monto de la segunda venta: ")
venta2= float (venta2)

venta3 = input("Ingresa el monto de la tercera venta: ")
venta2= float (venta3)

totalventas = (venta1 + venta2 + venta3)
totalventas = float

comisiontotal= (0.10 * totalventas) 
comisiontotal= float

totaldelmes= (sueldobase + comisiontotal)
totaldelmes = float
print("Dinero obtenido por concepto de COMISION por tres ventas: ", comisiontotal)
print("Dinero obtenido total del  mwes: ", totaldelmes)
