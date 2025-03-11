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


