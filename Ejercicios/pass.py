passw = False

while not passw:
    valor = input('Ingrese su nueva contraseña: ')
    if len(valor) >= 6:
        print('Contraeña valida')
        passw = True
    else:
        input('Invalido, debe tener minimo 6 caracteres')


