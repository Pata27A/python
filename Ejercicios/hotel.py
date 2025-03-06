print('*** RESERVA DE HOTEL ***')

nombre = input('Ingrese su nombre: ')
dias = int(input('Dias de estadia: '))
cuarto_vista = input('Cuarto con vista al mar? (SI/NO): ')

sin_vista_mar = 150.50
vista_al_mar = 190.50

resultado1 = dias * vista_al_mar
resultado2 = dias * sin_vista_mar

if cuarto_vista.strip().lower() == 'si':
    print('Escogio un cuarto con vista al mar')
    print(f'Dias de estadia: {dias}')
    print(f'Total a pagar: {resultado1:.2f}')
else:
    print('Escogio un cuarto sin vista al mar')
    print(f'Dias de estadia: {dias}')
    print(f'Total a pagar: {resultado2:.2f}')    