#import modulo_funcion_sumar
from modulo_funcion_sumar import sumar
#titulo
def titulo():
    print('*** FUNCIONES ****')

titulo()

#sintaxis definicion de una funcion
#1. Definicion de la funcion (verbo o accion)
def nombre_de_la_funcion (parametro1, parametro2):
#2.cuerpo de la funcion
    resultado = parametro1 + parametro2
    return resultado

#llamada de la funcion
resultado_final = nombre_de_la_funcion (5,3)
print (resultado_final)

#----------------------------------------------------
def saludar(mensaje): #firma del metodo
    #cuerpo de la funcion
    print(f'Mensaje Recibido: {mensaje}')


#llamar la funcion
titulo()
saludar('Hola a todos')

#---------------------------Modulos
titulo()

resultado_funcion = sumar(1, 1)
print(resultado_funcion)

#--------------------Aargumentos por nombres
titulo()

def personas(nombre, apellido, edad):
    print(f'Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}')

#Primero llamamos a funcion pasando los argumentos de manera posicional
personas('Ricardo', 'Quintana', 32)
#llamar la funcion usando argumentos por nombre
personas(nombre='Carlos', apellido='Rojas', edad=28)
#llamar la funcion usando argumentos por nombre pero intercambiando el orden
personas(nombre='Carlos', edad=28, apellido='Rojas' )

#--------------------regresar varios valores
titulo()
def persona_M(nombre, apellido, edad):
    return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = persona_M('sandra', 'perez', 20)
print(f'Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}')
#--------------------coordenadas
titulo()
def coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

#llamar la funcion
resultado = coordenadas()
print(resultado)

#unpacking
x1, y1, z1 = resultado
print(f'x {x1}, y {y1}, z {z1}')
#--------------------funciones recursivas
titulo()

def recursiva(numero):
    if numero == 1:
        print(numero, end=' ')
    else:
        print(numero, end=' ')
        recursiva(numero - 1)    
        

recursiva(5)