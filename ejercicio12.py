''' Ejercicio N°12

Ingresado un número X, calcular X5.

var: pot, x, i: integer; '''

pot = 1
x = int(input('Ingrese un número: '))
for i in range(1,6):
	pot = pot * x
	print(pot)