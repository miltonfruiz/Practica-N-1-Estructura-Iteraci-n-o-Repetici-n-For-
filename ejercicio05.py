''' Ejercicio N°5

Para 1000 usuarios residenciales de energía eléctrica se cuenta con pares de valores
que indican, para cada medidor, el consumo de Kilowatios al final del mes anterior y el 
consumo de Kilowatios al final del mes actual. Además se tiene el precio por Kilowatio. 
Exhibir, para cada usuario, el precio del Kilowatio, el consumo del mes y el importe a
abonar.

var: precio: float; i, kwa: integer;  '''

precio = float(input('Ingrese precio de kilowatio: '))
for i in range(1,1001):
	kwa = int(input('Ingrese total kilowatios consumidos: '))
	print('El precio del kilowatio es: ',precio)
	print('El consumo del mes es: ',kwa)
	print('El importe a abonar es: ',precio*kwa)