import sys
sys.path.append('/home/asanabria/Documents/python')

from PC.monitor import Monitor
from PC.dispositivos_entrada import Teclado
from PC.dispositivos_entrada import Raton

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.ID_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''
ID Computadora: {self.ID_computadora}
Nombre: {self.nombre}
{self.monitor}
{self.teclado}
{self.raton}
'''