def titulo():
    print('********************************************')
    print('*** POO ***')


#---------------------------------------------
titulo()
print('*** ERENCIA ***')

class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')

print('Clase Padre, soy Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\Soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
#------------------------------------------------
titulo()
class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')
#sobreescritura dormir de la clase padre
    def dormir(self):
        print('Duermo pocas horas')


print('Clase Padre, soy Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\Soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()#metodo sobreescrito de la clase hija
perro1.hacer_sonido()

#----------------------------------------------
titulo()
print('*** POLIMORFISMO ***')

class Animal:
    def hacer_sonido(self):
        print('Maullar')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')

class Gato(Animal):
    pass
    #def color(self):
     #   print('Gato Gris')


animal1 = Animal()
animal1.hacer_sonido()
#---------------------
perro1 = Perro()
perro1.hacer_sonido()
#-----------------------
gato1 = Gato()
gato1.hacer_sonido()
#gato1.color()
#----------------------------
titulo()
print('*** DUCKTYPING ***')
class Animal:
    def hacer_sonido(self):
        print('Maullar')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')

class Gato(Animal):
    pass
    #def color(self):
     #   print('Gato Gris')
#funcion polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

animal1 = Animal()
hacer_sonido_animal(animal1)
#---------------------
perro1 = Perro()
hacer_sonido_animal(perro1)
#-----------------------
gato1 = Gato()
hacer_sonido_animal(gato1)
#gato1.color()
#----------------------------
titulo()
print('***Clase Object ***')

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #metodo str------------
    def __str__(self):
        return f'''
Nombre {self.nombre}
Apellido {self.apellido}
'''
    
persona1 = Persona('Ana', 'Martinez')
print(persona1)#este metodo llama automaticamente desde el print


#metodo