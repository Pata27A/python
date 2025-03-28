

valor1 = float(input('Proporcione el pago sin impuesto: '))
valor2 = float(input('Proporcione el monto del impuesto: '))


def impuesto():
    resultado = valor1 + valor1 * (valor2/100)
    print(f'Pago con impuesto {resultado}')

impuesto()