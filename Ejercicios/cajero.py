inicial = 1000
salir = False
while not salir:
    print("""
    *** MENU ***
      Seleccione una opción:
            1 - Ver saldo
            2 - Realizar Retiro
            3 - Depositar
            4 - Salir
    """)
    opcion = int(input('Ingrese una opcion: '))
    if opcion == 1:
        print(f'Saldo en caja ${inicial}')
    elif opcion == 2:
        valor = int(input('Ingrese el valor del retiro: '))
        if valor <= inicial:
            inicial -= valor
            print(f'Valor retirado: ${valor}')
            print(f'Saldo en caja ${inicial}')
        else:
            print(f'Su saldo es insuficiente, Saldo actual ${inicial}')    
    elif opcion == 3:
        valor = int(input('Ingrese el valor a depositar: '))
        inicial += valor
        print(f'Tu saldo es: {inicial}')
    elif opcion == 4:
        print('Saliendo del Cajero')
        salir= True
    else:
        print('Opcion no valida')
