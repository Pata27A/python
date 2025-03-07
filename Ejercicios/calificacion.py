print('*** SISTEMA DE CALIFICACION ***')

calificacion = int(input('Ingrese la calificacion: '))

if calificacion >= 9 and calificacion <= 10:
    print(f'Tu calificacion es {calificacion}, obtuviste una A')
elif calificacion >= 8 and calificacion < 9:
    print(f'Tu calificacion es {calificacion}, obtuviste una B')
elif calificacion >= 7 and calificacion < 8:
    print(f'Tu calificacion es {calificacion}, obtuviste una C')
elif calificacion >= 6 and calificacion < 7:
    print(f'Tu calificacion es {calificacion}, obtuviste una D')
elif calificacion >= 0 and calificacion < 6:
    print(f'Tu calificacion es {calificacion}, obtuviste una F')
else:
    print('Valor Desconocido')