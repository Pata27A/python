print('*** SISTEMA DE INVENTARIO ***')

inventario = []
contador_id = 1

def agregar():
    global contador_id
    nombre = input('Ingrese el nombre del Producto: ')
    precio = int(input('Ingrese el Precio del Producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))

    producto = {
        'Id': contador_id,  # Cambio aquí para usar 'Id' con mayúscula
        'Nombre': nombre,
        'Precio': precio,
        'Cantidad': cantidad, 
    }

    inventario.append(producto)
    contador_id += 1
    print('Producto agregado exitosamente. \n')


def buscar():
    id_buscar = int(input('Ingrese el ID del producto: '))
    producto_encontrado = None
    for producto in inventario:
        if producto['Id'] == id_buscar:  # Cambié 'id' a 'Id'
            producto_encontrado = producto
            break
    if producto_encontrado:
        print(f'ID: {producto_encontrado["Id"]},\nNombre del Producto: {producto_encontrado["Nombre"]},\nPrecio: {producto_encontrado["Precio"]},\nCantidad: {producto_encontrado["Cantidad"]}')
    else:
        print(f'\nNo se encontró el producto con el ID proporcionado: {id_buscar}\n')

def mostrar_inventario():
    if inventario:
        print('*** Inventario Actualizado ***')
        for producto in inventario:
            print(f'ID: {producto["Id"]},\nNombre del Producto: {producto["Nombre"]},\nPrecio: {producto["Precio"]},\nCantidad: {producto["Cantidad"]}\n')
    else:
        print('El inventario está vacío.\n')
        
def menu():
    print('1. Agregar Producto')
    print('2. Buscar Producto por ID')
    print('3. Mostrar Inventario')
    print('4. Salir')


while True:
    menu()
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        agregar()
    elif opcion == '2':
        buscar()
    elif opcion == '3':
        mostrar_inventario()
    elif opcion == '4':
        print('Saliendo del Sistema....')
        break
    else: 
        print('Opción no válida. Intente nuevamente.')
