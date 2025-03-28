class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self.ID = Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano

    def __str__(self):
        return f'''
ID Monitor: {self.ID}
Marca: {self.marca}
Tamaño: {self.tamano}
'''
