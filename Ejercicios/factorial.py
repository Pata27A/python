print('*** FACTORIAL DEL NUMERO 5 ***')

def factorial(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado parcial {numero} es : 1')
        return 1 
    else:
        parcial = numero * factorial(numero - 1)
        print(f'Resultado parcial {numero} es: {factorial}')
        return parcial

numero = 5
resultado = factorial(5)
print(f'Resultado parcial {numero}, es {resultado}')
