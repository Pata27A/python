print('*** TIENDA EN LINEA ***')

monto_compra = float(input('Ingrese monto de la compra: '))
miembro = input('Eres mienbro (SI/NO): ')

if monto_compra >= 1000 and miembro.strip().lower() == 'si':
    descuento = monto_compra * 0.10
    total1 = monto_compra - descuento
    print('Felicidades, has obtenido un descuento del 10%')
    print(f'Monto de la compra: {monto_compra}')
    print(f'Descuento aplicado: {descuento}')
    print(f'Total a pagar: {total1}')
elif monto_compra <= 1000 and miembro.strip().lower() == 'si':
    descuento = monto_compra * 0.05
    total1 = monto_compra - descuento
    print('Felicidades, has obtenido un descuento del 5%')
    print(f'Monto de la compra: {monto_compra}')
    print(f'Descuento aplicado: {descuento}')
    print(f'Total a pagar: {total1}')
else:
    print(f'No aplica desceunto: {monto_compra}')