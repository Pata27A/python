print('*** DIBUJO DE TRIANGULO ***')

filas = int(input('Ingrese el numero de filas:  '))

for fila in range(1, filas + 1):
    espacios = ' ' * (filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios}{asteriscos}')