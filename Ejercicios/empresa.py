import sys
sys.path.append('/home/asanabria/Documents/python')

from Ejercicios.empleados import Empleado

class Empresa:

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []


    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)


    def obtener_numero_departamento(self, departamento):
        contador_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:  # Corrección aquí
                contador_por_departamento += 1
        return contador_por_departamento
    
    def obtener_total_por_empresa(self):
        print(f'\nTotal empleado en la empresa {self.nombre}')
        for empleado in self.empleados:
            print(f'''Empleado {empleado.id}
                      Nombre: {empleado.nombre}
                      Despartamento: {empleado.departamento}



''')
