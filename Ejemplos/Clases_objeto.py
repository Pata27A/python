def titulo():
    print('-----------------------------')
    print ('*** CLASES Y OBJETOS ***')


#clases y objetos
titulo()

class Persona:
    #constructor-----------------------------------------------
    def __init__(self, nombre, apellido):
        #creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    #def inicializar_persona(self, nombre, apellido):
        #creamos los atributos de la clase
    #    self.nombre = nombre
    #    self.apellido = apellido

    def mostrar_personas(self):
        print(f'''
            Nombre: {self.nombre}
            Apellido: {self.apellido}''')
#objetos-------------------------------------------
if __name__ == '__main__':
    #crear primer objeto
    persona1 = Persona('Layla', 'Acosta') #se crea un objeto vacio en memoria
    #persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_personas()
    print(f'Dir. memoria persona1: {id(persona1)}')
    print(f'Hex conversion: {hex(id(persona1))}')
       
    #crear segundo onjeto

    persona2 = Persona('Ivan', 'Sanchez')
    #persona2.inicializar_persona('Ivan', 'Sanchez')
    persona2.mostrar_personas()
    print(f'Dir. memoria persona2: {id(persona2)}')
    print(f'Hex conversion: {hex(id(persona2))}')


#Encasulapmiento------------------------------------
titulo()

class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca #atributo publico
        self._modelo = modelo #atributo protejido
        self.__color = color #atributo privado
        
    def conducir (self):
        print(f'''
            Marca: {self.marca}
            Modelo : {self._modelo}
            Color: {self.__color}
            ''')
        
if __name__ == '__main__':
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()

#--------------------------------------------------
titulo()

class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca 
        self._modelo = modelo #atributo protejido
        self._color = color 
        
    def conducir (self):
        print(f'''
            Marca: {self._marca}
            Modelo : {self._modelo}
            Color: {self._color}
            ''')
    #def get_marca(self):
    #    return self._marca
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    #def set_marca(self, marca):
    #    self._marca = marca
    #def get_modelo(self):
    #    return self._modelo
    @property
    def modelo(self):
        return self._modelo
    def set_marca(self, modelo):
        self._modelo = modelo
    def get_color(self):
        return self._color
    def set_marca(self, color):
        self._color = color
        
if __name__ == '__main__':
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
#----------------------------atributos clase instancia
titulo()

class Persona:
    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


if __name__ == '__main__':
    print(f'atributo de clase: {Persona.atributo_clase}')

    Persona.atributo_clase = 10

    print(f'atributo de clase: {Persona.atributo_clase}')

    persona1 = Persona(15)
    print(f'atributo de clase desde persona1: {Persona.atributo_clase}')
    print(f'atributo de instancia: {persona1.atributo_instancia}')

    persona2 = Persona(30)
    print(f'atributo de clase desde persona2: {Persona.atributo_clase}')
    print(f'atributo de instancia: {persona2.atributo_instancia}')
