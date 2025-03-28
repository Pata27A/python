print('*** SUSCRIPTORES ***')

suscriptores = set()
numero = int(input('Proporciona el numero de suscriptores inicales'))


for _ in range(numero):
    suscriptores.add(input('Nuevo suscriptor (email):'))
#suscriptores = {'lui@mail.com', 'dad@mail.com', 'pai@mail.com'}
print(f'Suscriptores: {suscriptores}')

nuevo = 'pa@mail.com'
if nuevo in  suscriptores:
    print(f'El suscriptor ya esta en la lista {nuevo}')
else: 
    suscriptores.add(nuevo)    
    print(f'El suscriptor se agrego a la lista. {nuevo}')
print(f'Suscriptores: {suscriptores}')

#eliminar
sus_eliminar = 'pa@mail.com'
suscriptores.remove(sus_eliminar)
print(f'El suscriptor ya se elimino {nuevo}')
print(f'Suscriptores: {suscriptores}')

#caantidad
print(f'cantidad de Suscriptores: {len(suscriptores)}')


print(f'LISTA DE SUSCRIPTORES')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')

#--------------------------------------------------------------
#Diccionario
persona = {
    'nombre': 'Pedro',
    'edad': 30,
    'casado': True}

print(f'Los valores son: {persona}')
print(f'Nombre: {persona["nombre"]}\nEdad: {persona["edad"]}\nCasado: {persona["casado"]}')

#Modificar el valor del diccionario
persona['edad'] = 35
print(f'Nombre: {persona["nombre"]}\nEdad: {persona["edad"]}\nCasado: {persona["casado"]}')
#agregar
persona['Profesion'] = 'ING'
print(f'Nombre: {persona["nombre"]}\nEdad: {persona["edad"]}\nCasado: {persona["casado"]}\nProfesion: {persona["Profesion"]}')

#eliminar
del persona['Profesion']
print(f'Los valores son: {persona}')

#iterar los elementos
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

#obtener valores

for  valor in persona.values():
    print(f'Valores : {valor}')
#obtener Laves

for  llave in persona.keys():
    print(f'LLave : {llave}')