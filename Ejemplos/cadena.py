#manejo de cadenas 
cadena1 = "Hola Mundo"
cadena1 = "Adios"
cadena2 = "Python es genial"
cadena3 = '''Este es un ejemplo de 
multiples lineas en cadena,
lleva 3 comillas simples'''
print(cadena1)
print(cadena2)
print(cadena3)

#Manejo de indices en cadena

cadena4 = 'Hola Mundo'
print(cadena4)
#-------------------------
primer_caracter = cadena4[0]
print(primer_caracter)

#Inmutabilidad de una cadena
cadena5 = "Hola MUndo"

print(cadena5)

#Caracteres especiales
print('Hola \nMundo') #\n salto de linea
print('\tHola Mundo') #\t tabulador
print('Hola \' Mundo') #\' para poner caracter especial
print("Hola \" Mundo") #\" para poner caracter especial

#Concatenacion de cadenas
#Metodo +
cadena6 = 'Hola'
cadena7 = 'Mundo'
concatenacion = cadena6 + ' ' +  cadena7
print(concatenacion)
#Metodo join
concatenacion = ''.join([cadena6, ' ' , cadena7])
#Formateo de cadenas
nombre = 'Juan'
edad = 30
#Metodo f-string
mensaje = f'Hola, me llamo {nombre} y tengo {edad} años'
print(mensaje)
#Metodo format
mensaje = 'Hola, me llamo {} y tengo {} años'.format(nombre,edad)
#Metodos de cadenas
cadena8 = 'Hola Mundo'
print(f'Cadena Original: {cadena8}')
mayusculas = cadena8.upper()
print(f'Cadena en MAYUSCULAS: {mayusculas}')
print(f'Cadena de minusculas: {cadena8.lower()}')
print(f'Cadena con espacios: {cadena8}')
print(f'Cadena sin espacios: {cadena8.strip()}')

#Obtener datos de una cadena
cadena9 = 'Hola, Mundo!'
largo = len(cadena9)
print(f'Largo de la cadena: {largo}')

#Obtener sub-cadena
cadena10 = 'Hola, Mundo!'
subcadena = cadena10[6:12]
print(f'Sub-Cadena: {subcadena}')

#Buscar sub-cadena
cadena11 = 'Hola, Mundo!'
posicion = cadena11.find("Mundo")
print(f'Indice de la Sub-Cadena: {posicion}')

#Reemplazar sub-cadena
cadena12 = 'Hola, Mundo!'
nueva_cadena = cadena12.replace("Mundo","a todos")
print(f'Nueva Sub-Cadena: {nueva_cadena}')

#Separar en sub-cadena
cadena13 = 'Hola, Mund,o!'
lista = cadena13.split(',')
print(f'Separar Sub-Cadena: {lista}')

#Multiplicacion en sub-cadena
cadena14 = 'Hola, Mundo!'
veces = 3
resultado = cadena14 * veces
print(f'Resultado: {resultado}')