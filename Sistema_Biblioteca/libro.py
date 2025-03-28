class Libro:

    contador = 0

    def __init__(self, titulo, autor, genero):
        self.id = Libro.contador
        Libro.contador += 1
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
    def mostrar_info(self):
        print(f'ID: {self.id}, Autor: {self.autor}, Titulo: {self.titulo}, Genero: {self.genero}')

    @classmethod
    def obtener_libros(cls):
        return cls.contador