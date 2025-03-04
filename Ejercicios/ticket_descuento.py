print('***GENERAR TICKET DE VENTA CON DESCUENTO***')

precio_leche = float(input(f'Precio de la leche: '))
precio_pan = float(input(f'Precio del pan: '))
precio_lechuga = float(input(f'Precio de la lechuga: '))
precio_platano = float(input(f'Precio del platano: '))

#calculo
subtotal = precio_leche + precio_lechuga + precio_pan + precio_platano

#menos descuento
descuento = subtotal * 0.10
total_aplicado = subtotal - descuento

#impuesto
imppuesto = total_aplicado * 0.16

#calculo con impuesto
costo_total_compra = total_aplicado + imppuesto


print(f'''
      SubTotal: ${subtotal:.2f}
      Descuento aplicado (10%): ${descuento:.2f}
      Impuesto (16%):  ${imppuesto:.2f}
      Costo total de la compra: ${costo_total_compra:.2f}
      ''')