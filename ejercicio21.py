''' Ejercicio N°21

Se tienen los siguientes datos de los N socios de un club:
Número de socio
Edad
Sexo (F ó M)
Importe de la cuota
AyED – Práctica Nº 1
Página 7 de 12
Se quiere saber:
a) Cantidad de mujeres y cantidad de hombres
b) Promedio de edad de todos socios
c) Total recaudado por el club en concepto de cuotas
 
var: cm, ch, total, socios, i, numero, edad: integer; promedio, importe: float; sexo: string; '''

cm = 0
ch = 0
promedio = 0
total = 0
socios = int(input('Ingrese cantidad de socios: '))
for i in range(1, socios+1):
	numero = int(input('Ingrese numero de socio: '))
	edad = int(input('Ingrese edad: '))
	sexo = str(input('Ingrese sexo, F o M: '))
	importe = float(input('Ingrese importe de la cuota: '))
	if sexo == 'F'or sexo == 'f':
		cm = cm + 1
	elif sexo == 'M' or sexo == 'm':
		ch = ch + 1
	else:
		print('No corresponde a un género.')
	promedio = promedio + edad
	total = total + importe
print('Cantidad de mujeres',cm,', cantidad de hombres',ch)
print('Promedio de edad de los socios',promedio/socios)
print('Total recaudado', total)