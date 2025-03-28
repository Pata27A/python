print('*** Potencia de numeros ***')

base = int(input('Ingrese la base a potenciar: '))
exponente = int(input('Ingrese el exponente: '))

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    # Caso recursivo
    else:
        return base * potencia(base, exponente - 1)

resultado = potencia(base, exponente)
print(f'El resultado de {base} elevado a {exponente} es: {resultado}')
