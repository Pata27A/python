print('*** SISTEMA BANCARIO ***')

continuar = input('Desea salir del SISTEMA (SI/NO): ')
resultado = not continuar.strip().lower() == 'si'

if resultado:
    print('Continuamos dentro del Sistema')
else:
    print('Saliendo del Sistema')    