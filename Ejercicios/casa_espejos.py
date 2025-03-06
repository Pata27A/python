print('*** CASA DE LOS ESPEJOS ***')

edad = int(input('Ingrese su edad: '))
edad_permitida = 10
miedo = input('Te da miedo la oscuridad (SI/NO): ')


if edad >= edad_permitida and not miedo.strip().lower() == 'si':
    print('Puedes Entrar')
else:
    print('No puedes entrar')