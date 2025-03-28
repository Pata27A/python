import sys
sys.path.append('/home/asanabria/Documents/python')

from Sistema_Biblioteca.libro import Libro
from Sistema_Biblioteca.biblioteca import Biblioteca



biblioteca1 = Biblioteca('*** BIENVENIDOS A LA BIBLIOTECA ***', 'TITULO', 'AUTOR')
biblioteca1.agregar_libros('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Narrativa')
biblioteca1.agregar_libros('El conde de Montecristo', 'Alexandre Dumas', 'Lírica')
biblioteca1.agregar_libros('Orgullo y Prejuicio', 'Jane Austen', 'Dramática')
biblioteca1.agregar_libros('Cumbres borrascosas', 'Emily Brontë', 'Ensayo')
biblioteca1.agregar_libros('La Odisea', 'Homero', 'Novela')

biblioteca1.buscar_autor()
biblioteca1.buscar_genero()
biblioteca1.todos_libros()