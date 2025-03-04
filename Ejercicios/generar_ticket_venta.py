print('***GENERACION TICKET DE VENTA***')
precio_leche = float(input(f'Precio de la leche: '))
precio_pan = float(input(f'Precio del pan: '))
precio_lechuga = float(input(f'Precio de la lechuga: '))
precio_platano = float(input(f'Precio del platano: '))

#calculo
subtotal = precio_pan + precio_leche + precio_lechuga + precio_platano

#impuesto
impuesto = subtotal * 0.16

#calcula
costo_total_compra = subtotal + impuesto

print(f'''
      SubTotal: ${subtotal:.2f}
      Impuesto (16%):  ${impuesto:.2f}
      Costo total de la compra: ${costo_total_compra:.2f}
      ''')