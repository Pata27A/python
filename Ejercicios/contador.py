class Persona:
    contador_persona = 0

    def __init__(self, nombre, apellido):
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido

    def mostar_personas(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')
    
    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo Estatico')
        return Persona.contador_persona

if __name__ == '__main__':
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostar_personas()
    persona2 = Persona('Angel', 'Sanabria')
    persona2.mostar_personas()


    print(f'Contador personas: {Persona.get_contador_personas_estatico()}')