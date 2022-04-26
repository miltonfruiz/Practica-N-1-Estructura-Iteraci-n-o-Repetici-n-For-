''' Ejercicio N°17

Incorporar al ejercicio anterior la búsqueda del valor mínimo y el orden en el que 
fueron ingresados.

var: numero, vmax, vmin, posM, posm, i: integer; '''

numero = int(input('Ingrese un numero: '))
vmax = numero
vmin = numero
posM = 1
posm = 1
for i in range(2, 94):
	numero = int(input('Ingrese un numero: '))
	if numero > vmax:
		vmax = numero
		posM = i
	if numero < vmin:
		vmin = numero
		posm = i
print('El valor máximo es ',vmax,'y está en la posición ',posM)
print('El valor mínimo es ',vmin,'y está en la posición ',posm)