#Sentencia if
edad = 30
if edad >= 18:
    print('Eres mayor de edad') 

#Sentencia if else
edad = 30
if edad >= 18:
    print(f'Eres mayor de edad, tienes {edad}')
else:
    print(f'Eres menor de edad, tienes {edad}') 

#Sentencia if elif else
edad = 15
if edad >= 18:
    print(f'Eres mayor de edad, tienes {edad}')
elif 13 <= edad < 18:
    print(f'Eres un adolecente, tienes {edad}')    
else:
    print(f'Eres un niño, tienes {edad}') 
#-------------------------------------------------------------------------------------------------------
#operador ternario
edad= int(input('Ingrese su edad: '))

adulto = 'si' if edad >= 18 else 'no'

print(f'Es un adulto {adulto}')
