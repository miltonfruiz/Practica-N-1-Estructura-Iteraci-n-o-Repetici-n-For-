''' Ejercicio N°22

Se cuenta con un texto de 190 caracteres. Determinar cuantas veces aparece la sílaba 
“pa”.
 
var: contador: integer; caracter1, caracter2: string; '''

contador = 0
caracter1 = str(input('Ingrese el caracter: '))
for i in range(1,5):
	caracter2 = str(input('Ingrese el caracter: '))
	if caracter1 == 'p' and caracter2 == 'a':
		contador = contador + 1
print('Aparece ',contador,'veces.')