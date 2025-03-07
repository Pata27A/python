
salir = False

while not salir:
    print("""
    *** MENU ***
      Seleccione una opción:
            1 - Suma
            2 - Resta
            3 - Multiplicacion
            4 - Division
            5 - Salir
    """)
    
    try:
        opcion = int(input('Ingrese una opción: '))
        
        if opcion == 5:
            print('Saliendo...')
            salir = True
            continue
        
        valor1 = int(input('Ingrese valor 1: '))
        valor2 = int(input('Ingrese valor 2: '))

        if opcion == 1:
            resultado = valor1 + valor2
            print(f'Suma Total: {resultado}')
        elif opcion == 2:
            resultado = valor1 - valor2
            print(f'Resta Total: {resultado}')
        elif opcion == 3:
            resultado = valor1 * valor2
            print(f'Multiplicación Total: {resultado}')
        elif opcion == 4:
            if valor2 == 0:
                print("Error: No se puede dividir por cero.")
            else:
                resultado = valor1 / valor2
                print(f'División Total: {resultado:.2f}')
        else:
            print('Opción no válida, intente de nuevo.')
    
    except ValueError:
        print("Error: Ingrese solo números enteros.")
