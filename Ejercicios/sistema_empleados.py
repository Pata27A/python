#Entrada de datos por consola
print('***SISTEMA DE EMPLEADOS***')
nombre_apellido = input('Ingrese Nombre y Apellido: ')
edad = int(input('Ingrese su edad: '))
salario = float(input('Ingrese salario: '))
jefe_departamento = input("Es Jefe de Departamento (Si/NO): ")
#cONVERTIR jefe_departamento 
jefe_departamento = jefe_departamento.lower() == 'si'


print(f'Nombre y Apellido: {nombre_apellido} \nEdad: {edad} \nSalario del Empleado: {salario:,.0f} \nJefe de Departamento: {jefe_departamento}'.replace(',', '.'))

# Formatear el salario con puntos como separadores de miles
#salario_formateado = f'{salario:,.0f}'.replace(',', '.')