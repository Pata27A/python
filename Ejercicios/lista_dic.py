print('*** CONVINACION DE LISTAS Y DICCIONARIO ***')


agenda = []

agenda.append({'Nombre': 'Julio','Telefono': '+595','email': '@gmail.com','Direccion': 'Gral. Aquino'})
agenda.append({'Nombre': 'Maria','Telefono': '+595','email': '@.com','Direccion': 'Gral. Resquin'})

print(f'Persona: {agenda[1]}')
for contacto in agenda:
    print(f'Persona: {contacto["Nombre"]}')
    print(f'Teléfono: {contacto["Telefono"]}')
    print(f'Email: {contacto["email"]}')
    print(f'Dirección: {contacto["Direccion"]}')
    print('---')