import sys
sys.path.append('/home/asanabria/Documents/python')

from Sistema_Biblioteca.libro import Libro


class Biblioteca:


    def __init__(self, nombre, autor, genero):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.libros = []

    def agregar_libros(self, titulo, autor, genero):
        libro = Libro(titulo, autor, genero)
        self.libros.append(libro)

    def buscar_autor(self):
        print(f'\nAutor {self.autor}')
        for auto in self.libros:
            print(f'''ID {auto.id}
                      Autor: {auto.autor}#
                      Titulo: {auto.titulo}
                      Genero: {auto.genero}
''')
    def buscar_genero(self):
        print(f'\nAutor {self.genero}')
        for gene in self.libros:
            print(f'''ID {gene.id}
                      Autor: {gene.autor}
                      Titulo: {gene.titulo}
                      Genero: {gene.genero}#
''')
    def todos_libros(self):
        print(f'\nLista de libros en la biblioteca {self.nombre}:')
        for libro in self.libros:
            libro.mostrar_info()


# Definir la clase
class Saludar:
    # Definir el método
    def saludar(self):
        print('Hola Mundo')

# Crear una instancia de la clase
saludo = Saludar()

# Llamar al método usando la instancia
saludo.saludar()