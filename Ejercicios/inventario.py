print('*** SISTEMA DE INVENTARIO ***')

inventario = []
contador_id = 1

cantidad_productos = int(input('Cuantos productos desea agregar?: '))

for _ in range(cantidad_productos):

    nombre = input('Ingrese el nombre del Producto: ')
    precio = int(input('Ingrese el Precio del Producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))

    producto = {
        'Id': contador_id,
        'Nombre': nombre,
        'Precio': precio,
        'Cantidad': cantidad
    }

    inventario.append(producto)

    contador_id += 1

for producto in inventario:
    print(f'ID: {producto["Id"]},\nNombre del Producto: {producto["Nombre"]},\nPrecio: {producto["Precio"]},\nCantidad: {producto["Cantidad"]}')


#buscar
id_buscar = int(input('Ingrese el ID del pruducto a Buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto['Id'] == id_buscar:
        producto_encontrado = producto
        break
if producto_encontrado:
        print(f'ID: {producto_encontrado["Id"]},\nNombre del Producto: {producto_encontrado["Nombre"]},\nPrecio: {producto_encontrado["Precio"]},\nCantidad: {producto_encontrado["Cantidad"]}')

else:
    print(f'\nNo se encontro el producto con el ID proporcionado: {id_buscar}')

#Actualizado
print('*** Inventario Actualizado ***')
for producto in inventario:
    print(f'ID: {producto["Id"]},\nNombre del Producto: {producto["Nombre"]},\nPrecio: {producto["Precio"]},\nCantidad: {producto["Cantidad"]}')
