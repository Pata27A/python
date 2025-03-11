print('*** REPETICION DE UN MENSAJE ***')
mensaje = input('Ingresa el mensaje a repetir: ')
repeticion = int(input('Proporciona el numero de repeticiones: '))

for i in range(repeticion):
    print(f'{i+1} - {mensaje}')