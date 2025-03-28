class Dispositivos:
    def marca(self):
        return 'SAMSUNG'

    def tipo_entrada(self):
        return 'USB'

# Clase Raton (hereda de Dispositivos)
class Raton(Dispositivos):
    contador_raton = 0

    def __init__(self):
        Raton.contador_raton += 1
        self.id_raton = Raton.contador_raton

    def __str__(self):
        return f'''
ID Ratón: {self.id_raton}
Marca: {self.marca()}  
Tipo de Entrada: {self.tipo_entrada()}
'''

# Clase Teclado (hereda de Dispositivos)
class Teclado(Dispositivos):
    contador_teclado = 0

    def __init__(self):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado

    def __str__(self):
        return f'''
ID Teclado: {self.id_teclado}
Marca: {self.marca()}  
Tipo de Entrada: {self.tipo_entrada()}
'''  