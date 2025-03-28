class Empleado:
    contador_empleado = 0

    def __init__(self, nombre, departamento):
        Empleado.contador_empleado += 1
        self.id = Empleado.contador_empleado
        self.nombre = nombre
        self.departamento = departamento

    @classmethod
    def contador_empleados_estaticos(cls):
        return cls.contador_empleado
    