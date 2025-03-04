print('***SISTEMA DE PRESTAMO DE LIBRO***')

distancia = 3
credencial = input('Cuentas con credencial de estudiante (SI/NO)? :')
kilometros = int(input('Cuantos kilometros vives de la biblioteca :'))

prestamo = credencial.strip().lower() == 'si' or kilometros <= distancia

print(f'Tienes acceso al Prestamo: {prestamo}') 