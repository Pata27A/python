print('*** SALUD Y FITNESS***')

nombre = input('Ingrese su nombre: ')
pasos = int(input('Ingrese los pasos del dia: '))


meta_pasos = 10000
calorias_paso = 0.04

calorias_quemadas = pasos * calorias_paso

meta = 'SI' if pasos >= meta_pasos else 'NO'

print(f'Nombre {nombre}')
print(f'{pasos} pasos realizados')
print(f'{meta} se alcanzo la meta')
print(f'{calorias_quemadas} de calorias quemadas')