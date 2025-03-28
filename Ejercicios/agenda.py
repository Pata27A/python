print('*** AGENDA DE CONTACTOS ***')

agenda = {
    'Julio' : {
        'Telefono': '+595',
        'email': '@gmail.com',
        'Direccion': 'Gral. Aquino'
    },
    'Maria' : {
        'Telefono': '+595',
        'email': '@hotmail.com',
        'Direccion': 'Gral. Elizardo'
    }
}

print(f'Agenda: {agenda}')

#acceder a la informacion de un contacto en especifico
print(f'Contacto de Maria: {agenda["Maria"]["Telefono"]}')

#nuevo contacto
agenda['Ana'] = {
    'Telefono': '+595',
    'email': '@.com',
    'Direccion': 'Gral.Resquin'
}
print(f'Agenda: {agenda}')
#iterar contactos
for nombre, detalle in agenda.items():
    print(f'''Nombre: {nombre}
Telefono: {detalle.get('Telefono')}
Email: {detalle.get('email')}
Direccion: {detalle.get('Direccion')}
''')