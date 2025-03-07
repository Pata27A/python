print('*** SISTEMA DE ENVIOS ***')

nacional = 10
internacional = 20

destino = input('Ingrese su destino (NACIONAL/INTERNACIONAL): ')
peso = int(input('Ingrese el paquete en KILOGRAMOS: '))

if destino.strip().lower() == 'nacional':
    resultado = nacional * peso
    print(f'El costo del envio es: {resultado}')
else:
    resultado = internacional * peso
    print(f'El costo del envio es: {resultado}')