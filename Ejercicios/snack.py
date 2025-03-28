print('*** MAQUINA DE SNACKS ***')

def mercaderia():
    return {
        1: {'nombre': 'PAPAS', 'precio': 1000},
        2: {'nombre': 'REFRESCO', 'precio': 2000},
        3: {'nombre': 'SANDWICH', 'precio': 3000},
    }

def compra():
    carrito = []  # Lista para almacenar los productos seleccionados
    productos = mercaderia()

    while True:
        print("\nLista de Productos:")
        for codigo, datos in productos.items():
            print(f"{codigo}. {datos['nombre']} - {datos['precio']} Gs")

        try:
            codigo = int(input("\nIngrese el número del producto (0 para finalizar): "))
            if codigo == 0:
                break
            if codigo not in productos:
                print("Código inválido, intente de nuevo.")
                continue

            carrito.append(productos[codigo])  # Agregar el producto al carrito

        except ValueError:
            print("Entrada no válida, por favor ingrese números.")

    # Mostrar resumen de la compra
    print("\nResumen de la compra:")
    total = sum(item['precio'] for item in carrito)  # Sumar precios de los productos
    for item in carrito:
        print(f"{item['nombre']} - {item['precio']} Gs")

    print(f"\nTotal a pagar: {total} Gs")

def buscar():
    productos = mercaderia()  # Obtener el diccionario de productos
    try:
        id_buscar = int(input('Ingrese el ID del producto: '))
        producto_encontrado = productos.get(id_buscar)
        if producto_encontrado:
            print(f'ID: {id_buscar},\nNombre del Producto: {producto_encontrado["nombre"]},\nPrecio: {producto_encontrado["precio"]} Gs')
        else:
            print(f'\nNo se encontró el producto con el ID proporcionado: {id_buscar}\n')
    except ValueError:
        print("Entrada no válida, por favor ingrese un número.")

def menu():
    print('1. Mostrar Snacks')
    print('2. Comprar Snacks')
    print('3. Buscar Producto')
    print('4. Salir')

while True:
    menu()
    opcion = input('Seleccione una opcion: ')

    if opcion == '1':
        productos = mercaderia()
        print("\nLista de Snacks:")
        for codigo, datos in productos.items():
            print(f"{codigo}. {datos['nombre']} - {datos['precio']} Gs")
    elif opcion == '2':
        compra()
    elif opcion == '3':
        buscar()
    elif opcion == '4':
        print('Saliendo del sistema....')
        break
    else:
        print('Opción no válida. Intente nuevamente.')
