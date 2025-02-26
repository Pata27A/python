#Sistema Generador de ID Unico
from random import randint


nombre = input('Ingrese su Nombre: ')
#Buscar las dos primeras letras
nombre1 = nombre[0:2].upper()
#------------------------------------
apellido = input('Ingrese su Apellido: ')
#Buscar las dos primeras letras
apellido1 = apellido[0:2].upper()
#------------------------------------
aho = input('Ingrese su Año de nacimiento (AÑO): ')
#Buscar los dos ultimos digitos
aho1 = aho[2:4]
#Numeros aleatorios
numero1 = randint(0, 9 )
numero2 = randint(0, 9 )
numero3 = randint(0, 9 )
numero4 = randint(0, 9 )


print(f'***Su ID DE USUARIO ES: {nombre1}{apellido1}{aho1}{numero1}{numero2}{numero3}{numero4}***')