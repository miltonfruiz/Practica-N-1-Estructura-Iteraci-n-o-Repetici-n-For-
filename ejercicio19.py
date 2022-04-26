''' Ejercicio N°19

Dada una sucesión de N números enteros ordenados en forma creciente, no
consecutivos, hallar la máxima diferencia entre dos números sucesivos

var: mdif, N, numero, i, siguiente, dif: integer; '''

mdif = 0
N = int(input("Ingrese cantidad de números de la secuencia: "))
numero = int(input("Ingrese un número: "))
for i in range(N-1):
	siguiente = int(input("Ingrese el siguiente número: "))
	dif = siguiente - numero
	if dif > mdif:
		mdif = dif
		numero = siguiente
print("La máxima diferencia entre dos números es:", mdif)