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


#--------------------------------------------------------------------------------------
#Ausencia de valor
nombre = None
while not nombre:
    nombre = input('Ingresa tu nombre de usuario: ')

print(f'Nombre de usuario valido: {nombre}')

#--------------------------------------------------------------------------------------
#Funcion Range, es una funcion incorporada que genera una secuencua de numeros, se utiliza en FOR

for i in range(5):
    print(i)


for i in range(0, 10, 2):
    print(i)
#--------------------------------------------------------------------------------------
#Break y continue
#break
for nummero in range(1, 10):
    if nummero % 2 == 0:
        print(nummero)
        break #salir del ciclo

#continue
for nummero in range(1, 10):
    if nummero % 2 == 1:
        continue #salir del ciclo
    print(nummero)