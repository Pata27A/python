print('*** MAYOR D EDOS NUMEROS PROPORCIONADOS ***')

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))

if numero1 > numero2:
    print(f'Primer numero: {numero1}')
    print(f'Segundo numero: {numero2}')
    print(f'Numero mayor es: {numero1}')
elif numero1 == numero2:
    print(f'Los numeros son iguales {numero1}, {numero2}')    
else:
    print(f'Primer numero: {numero1}')
    print(f'Segundo numero: {numero2}')
    print(f'Numero mayor es: {numero2}')    