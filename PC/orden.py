import sys
sys.path.append('/home/asanabria/Documents/python')

from PC.computadora import Computadora
from PC.monitor import Monitor
from PC.dispositivos_entrada import Teclado
from PC.dispositivos_entrada import Raton

class Ordenes:
    contador_ordenes = 0

    def __init__(self):
        Ordenes.contador_ordenes += 1
        self.ID_ordenes = Ordenes.contador_ordenes
        self.computadoras = []

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = "\n".join(str(comp) for comp in self.computadoras)
        return f'''
ID Orden: {self.ID_ordenes}
Computadoras:
{computadoras_str}
'''
    

#PRUEBAS
monitor1 = Monitor("LG", "24 pulgadas")
teclado1 = Teclado()
raton1 = Raton()

computadora1 = Computadora("DELL XPS", monitor1, teclado1, raton1)
computadora2 = Computadora("MACBOOK PRO", monitor1, teclado1, raton1)

orden1 = Ordenes()
orden1.agregar_computadora(computadora1)
orden1.agregar_computadora(computadora2)

print(orden1)