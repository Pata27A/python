print('*** SISTEMA DE AUTENTICACION ***')

usu = input('Ingrese su usuario: ')
passw = input('Ingrese su contraseña: ')

usu1 = 'angel'
passw1 = 'adsf'

if usu == usu1 and passw == passw1:
    print('Bienvenido al Sistema')
elif usu != usu1 and passw == passw1:
    print('Usuario invalido, vuelva a ingresar su usuario')
    usu = input('Ingrese su usuario: ')
    if usu == usu1:
        print('Bienvenido al Sistema')
elif usu == usu1 and passw != passw1:
    print('Contraseña invalida, vuelva a ingresar su contraseña')
    passw = input('Ingrese su contraseña: ')
    if passw == passw1:
        print('Bienvenido al Sistema')
else:
    print ('Los valores ingresados son incorrectos')
    usu = input('Ingrese su usuario: ')
    passw = input('Ingrese su contraseña: ')
    if usu == usu1 and passw == passw1:
        print('Bienvenido al Sistema')

