#Listas en python
numeros = [1, 2, 3, 4, 5]
print(f'{numeros}-> Lista original')
#Largo de la lista
print(f'Largo de la lista: {len(numeros)}')
#elementos de la lista
print(f'Acceder al valor del indice 4: {numeros[4]}')
print(f'Acceder al ultimo valor del indice: {numeros[-1]}')
#modificar los elementos de una lista
numeros[1] = 10 
print(f'Modificamos el valor: {numeros [1]}')
#agregar un nuevo elemento al final de la lista
numeros.append(6)
print(f'Agregar un nuevo elemento: {numeros} ')
#añadir un nuevo elemnto en un indice especifico
numeros.insert(2,15)
print(f'Añadir valor: {numeros}')
#eliminar elementos
numeros.remove(5)#por elemento
print(f'{numeros} se removio el valor 5')
#metodo pop
numeros.pop(1)#por indice
print(f'{numeros} se removio el indice 1')
#metodo del
del numeros[2]#por indice
print(f'{numeros} se removio el indice 1')
#sub-lista
sub_lista = numeros[1:3]
print(f'{sub_lista} sublista')
#iterar lista
nombres = ["Karla", "juan", "Laura"]
for nombre in nombres:
    print(nombre)

mixta = [1, "dos", 3.0, [4, 5]]
print()
for mix in mixta:
    print(mix)
#TUPLAS son similares a listas, la diferencia son inmutables.Datos que no se pueden modificar 
tuplas_numeros = (1, 2, 3, 4, 5)
print(tuplas_numeros)

for elemento in tuplas_numeros:
    print(elemento, end=(' '))
tuplas_mixta = ('manzana', 10, 3.14, [1, 2, 3])
print(f'Tupla anidada: {tuplas_mixta[1]}')
print(f'Tupla anidada: {tuplas_mixta[2]}')
print(f'Tupla anidada: {tuplas_mixta[3]}')

tupla_sin_parentesis = 'JUAN', 'kARLA'
print(f'\nCoordenadas en el eje X: {tupla_sin_parentesis[0]}')
print(f'\nCoordenadas en el eje X: {tupla_sin_parentesis[1]}')


tupla_un_elemento = 10,  #la coma no es opcional si o si debe llevar 
print(f'Tupla de un elemento: {tupla_un_elemento}')

#desempaquetado de tuplas
producto = ('P001', 'Camisa', 20.000)
id, descripcion, precio = producto
print(f'EL ID es: {id}\nLa descripcion es: {descripcion}\nel precio es: {precio:.3f}')

#convinacion de listas y tuplas
#definir una lista que almacena tuplas de productos
productos = [('P001', 'Camisa', 20.000),('P002', 'Jeans', 30.000),('P003', 'Sudadera', 40.000)]
#imprimie los valores y calcular el precio total
total = 0

print('Informacion de los productos:')
for producto in productos:
    id, descripcion, precio = producto
    total += precio
    print(f'Id: {id}\nDescripcion: {descripcion}\nPrecio: {precio:.3f} gs.')
print(f'Costo total: {total:.3f} gs.')

#set, son conjuntos de datos no ordenados
#set_a = {1, 2, 3, 4,}
#set_b = {3, 'Juan', True, 6.5}
numeros = {1, 2, 2, 3, 4}
print(numeros)
numeros.add(6)
print(numeros)
numeros.remove(6)
print(numeros)

for elemento in numeros:
    print(elemento, end='\n')
#comprobar si existe un elemento en el sets
print(f'Existe el elemento 4 en el sets?: {4 in numeros}')
 