print('*** OPERACIONES CON SET ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union: {union}')

interseccion = a & b
print(f'Interseccion: {interseccion}')

diferencia = a - b
print(f'Diferencia: {diferencia}')