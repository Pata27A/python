print('*** VALIDACION DE USUARIO***')

user1 = input('Ingrese su Usuario: ')
password1 = input('Ingrese la Contraseña: ')
user = 'angel'
password = 'adsf'


validacion = user1.strip() == user and password1 == password

print(f'''
      Validacion de Usuario: {validacion}
      ''')