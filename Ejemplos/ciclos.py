# while repite una serie de intrucciones mientras la condicion a evaluar sea verdadera
contador = 1
while contador <= 10:
    print(contador, end=' - ')
    contador += 1
#--------------------------------------------------------------------------------------
# for recorre una secuencia de valores, por ejemplo los caracteres de una cadena, una lista, etc
#ejecura un bloque de codigo por cada elemento de la secuencia;

cadena = 'Hola Mundo'
for letra in cadena:
    print(letra, end=' ')
 
frutas = ['platano', 'fresa', 'hongo']
for fruta in frutas:
    print(fruta, end=' ')