print('***SISTEMA DE DESCUENTO VIP***')

nro_productos = 10
cantidad = int(input('Cuantos productos compraste hoy :'))
membresia = input('Tiene la membresia (SI/NO) :')

descuento = cantidad >= nro_productos and membresia.strip().lower() == 'si'

print(f'Tienes acceso al descuento: {descuento}')