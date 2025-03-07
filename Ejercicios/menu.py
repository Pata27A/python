salir = False

while not salir:
    print("""
    *** MENU ***
      Seleccione una opción:
            1 - Crear Cuenta
            2 - Eliminar Cuenta
            3 - Salir
    """)
    
    try:
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            print('Creando tu cuenta...\n')
        elif opcion == 2:
            print('Eliminando tu cuenta...\n')
        elif opcion == 3:
            print('Saliendo...\n')
            salir = True
        else:
            print('Opción no válida, intenta de nuevo...\n')
    except ValueError:
        print("Error: Ingresa un número válido.\n")
