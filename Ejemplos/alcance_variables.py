def titulo():
    print('*** ALCANCE DE VARIABLES ***')

#-----------------------------------------------
titulo()

contador_golbal = 0

def incrementar():
    #Declaramos una variable local
    contador_local = 0
    global contador_golbal
    contador_golbal += 1

    contador_local += 1

    print(f'Local {contador_local}, Global {contador_golbal}')

#llamar la funcion
incrementar()
incrementar()
incrementar()

print(f'Global: {contador_golbal}')

#------------------------------------------args
titulo()

def super_heroes(super, nombre, *args):
    print(f'Super: {super} - {nombre} - {args}')
    for heroe in args:
        print(f'\tHeroes: {heroe}')
#llamar la funcion
super_heroes('Variable', 'Variable 2', 'Variable 3', 'Variable 4')

#--------------------------------argumentos variable en forma de kwargs
titulo()
def prueba_prueba2(nombre, *args, **kwargs):
    print(f'prueba: {nombre} - {args} - mas info {kwargs}')

#llamar la funcion
prueba_prueba2('Prueba1', 'Prueba2', edad=17, empresa='Lincoln')

#--------------------------------suma argumentos variable
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(f'Resultado: {resultado}')
#--------------------------------argumentos variable en forma de kwargs
def imprimir_detalle (**kwargs):
    print('\Valor Recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

imprimir_detalle(nombre='Karla', edad=30, ciudad='Luque')

