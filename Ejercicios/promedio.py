print('*** PROMEDIO DE CALIFICACIONES ***')

cantidad = int(input('Ingrese el numero de calificaciones a evaluar: '))
calificaciones = []
for cal in range(cantidad):
    calificacion = int(input(f'Calificacion {cal}: '))
    calificaciones.append(calificacion)
    promedio = sum(calificaciones) / cantidad
print(f'El promedio de las calificaciones es. {promedio}')