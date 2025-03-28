import sys
sys.path.append('/home/asanabria/Documents/python')

from Ejercicios.empresa import Empresa
from Ejercicios.empleados import Empleado






empresa1 = Empresa('Lincoln')
empresa1.contratar_empleado('Angel', 'TI')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Ana', 'RRHH')
empresa1.contratar_empleado('Julio', 'Ventas')

print(f'Empleados en total: {Empleado.contador_empleados_estaticos()}')


print(f'Ventas: {empresa1.obtener_numero_departamento("Ventas")}')


empresa1.obtener_total_por_empresa()