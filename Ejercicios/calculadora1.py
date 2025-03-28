print('*** Calculadora ***')






def sumar(variable1, variable2):

    resultado = variable1 + variable2
    print(f'El resultado de la suma es: {resultado}')

def restar(variable1, variable2):
    resultado = variable1 - variable2
    print(f'El resultado de la resta es: {resultado}')


def multiplicacion (variable1, variable2):
    resultado = variable1 * variable2
    print(f'El resultado de la multiplicacion es {resultado}')

def division (variable1, variable2):
    if variable2 != 0:
        resultado = variable1 / variable2
        print(f'El resultado de la division es {resultado}')
    else:
        print('No se puede dividir por cero')

def menu():
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Salir')


while True:
    menu()
    opcion = input('Selecciones una opcion: ')

    if opcion in ['1', '2', '3', '4']:
        variable1 = float(input('Ingrese el primer número: '))
        variable2 = float(input('Ingrese el segundo número: '))

    if opcion == '1':
        sumar(variable1, variable2)
    elif opcion == '2':
        restar(variable1, variable2)
    elif opcion == '3':
        multiplicacion(variable1, variable2)
    elif opcion == '4':
        division(variable1, variable2)
    elif opcion == '5':
        print('Saliendo del sistema...')
        break
    else:
        print('Opcion no valida')