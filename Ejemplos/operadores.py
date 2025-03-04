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
a,b = 10, 15
print (f'Valor inical de a: {a} \nValor inical de B: {b}')
#operador compuesto de suma +=
a += b # a = a + b
print (f'Operador a += b es: {a}')
#operador compuesto de resta -=
a = 10
a -= b # a = a - b
print (f'Operador a -= b es: {a}')
#operador compuesto de resta *=
a = 10
a *= b # a = a * b
print (f'Operador a *= b es: {a}')
#operador compuesto de resta /=
a = 10
a /= b # a = a / b
print (f'Operador a /= b es: {a}')
#operador compuesto de resta **=
a = 10
a **= b # a = a ** b
print (f'Operador a **= b es: {a:.2f}')
#---------------------------------------------
#operador de comparacion
a,b = 7, 5
print(f'Valor inical a: {a}, b: {b}')
#operador de comparacion-----igualdad ==
resultado = a == b
print(f'Resultado: {resultado}')
#operador de comparacion-----distinto !=
resultado = a != b
print(f'Resultado: {resultado}')
#operador de comparacion-----menor que <
resultado = a < b
print(f'Resultado: {resultado}')
#operador de comparacion-----menor o igual que <=
resultado = a <= b
print(f'Resultado: {resultado}')
#operador de comparacion-----mayor que >
resultado = a > b
print(f'Resultado: {resultado}')
#operador de comparacion-----mayor o igual que >=
resultado = a >= b
print(f'Resultado: {resultado}')
#operador logicos
condicion1 = False
condicion2 = False
#operador logicos and
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')
#operador logicos or
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2}: {resultado}')
#operador logicos not
resultado = not condicion1
print(f'Resultado {condicion1}: {resultado}')
#
nombre = ''
cadena_vacia = not nombre
print(f'\nLa variable no tiene ningun valor? {cadena_vacia}')
#
variable = None
variable_valor = not variable
print(f'La variable no tiene ninguna valor? {variable_valor}')
#Una variable se encuentra dentro del rango
dato = int(input('Proporciona un dato entero:'))
esta_dentro_rango = 1 <= dato <= 10
print(f'Variable esta dentro del rango: {esta_dentro_rango}')

esta_fuera_rango = not (1 <= dato <= 10)
print(f'Variable esta fuera del rango: {esta_fuera_rango}')