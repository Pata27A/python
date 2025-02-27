#operadores aritmeticos
a = 10
b = 3
#Suma
suma = a + b
print(suma)
#Resta
resta = a - b
print(resta)
#Multiplicacion
multiplicacion = a * b
print(multiplicacion)
#Division
division = a / b
print(f'{division:.2f}')
#Division Entera
div_entera = a // b
print(div_entera)
#Exponente-modulo
exponente = a ** b
print(exponente)
#---------------------------
#operadores de asignacion
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde python'
print(f'Valor de cadena: {cadena}')
#operadores de asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x: {x} Valor de y: {y} Valor de x: {z}')
#intercambio de valores de una variable, sin utilizar variables temporables
x, y = 5, 10
print(f'Valor de x: {x} Valor de y: {y}')
#aplicando el concepto de asignacion multiple pra intercambiar valores
x, y = y, x
print(f'Valor de x: {x} Valor de y: {y}')
#resibir multiples valores en input
nombre, apellido = input('Ingresa nombre y apellido separados por coma : ').split(',')
print(f'Nombre: {nombre} apellido: {apellido}')
#operadores de asignacion encadenada
a = b = c = 5
print(f'Valor de a: {a} Valor de b: {b} Valor de c: {c}')
#operadores de asignacion compuesto