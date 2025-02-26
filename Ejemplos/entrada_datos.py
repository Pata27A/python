#Conversiòn de Tipos de Datos
#Conversiòn de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print (f'Valor numerico en cadena:  {numero_cadena}')
print (f'Cadena a Entero:  {numero_entero}')

#Conversiòn de cadena a flotante
numero_cadena = '3.14'
numero_flotente = float(numero_cadena)
print (f'Valor numerico en cadena:  {numero_cadena}')
print (f'Cadena a flotante:  {numero_flotente}')

#Conversiòn de numeros a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print (f'Valor numerico:  {numero_entero}')
print (f'Numerico a cadena:  {numero_cadena}')

#Conversiòn a booleano
#Tipo boll es falso en los siguientes casos
#si el valor es 0, cadena vacia, o none, entonces regresa false
#Regresa true, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de none
#False
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor Booleano de 0:  {booleano}')#False
#True
numero_entero = 1
booleano = bool(numero_entero)
print(f'Valor Booleano de 1:  {booleano}')#True
#Cadena vacia
cadena_vacia = ''
booleano = bool(cadena_vacia)
print(f'Valor Booleano de 0:  {booleano}')#False
#Cadena vcon valor
cadena_valor = 'Angel'
booleano = bool(cadena_valor)
print(f'Valor Booleano de 0:  {booleano}')#True


#Entrada de datos por consola
nombre = input('Ingrese Nombre: ')
print(f'Nombre: {nombre}')

#Entrada de datos por consola edad al usuario entra como cadena y lo convertimos a numero
edad = int(input('Ingrese Edad: ') )
print(f'Edad: {edad}, y en un año tendras: {edad + 1}')

#Valores Aleatorios con la funcion ranint
#import random
from random import randint
#generar un numero aleatorio entre 1 y 10
numero = randint(1, 10)
print(f'NUmero aleatorio entre 1 y 10:  {numero}')

#dado
dado = randint(1, 6)
print(f'Resultado de lanzar el dado:  {numero}')


