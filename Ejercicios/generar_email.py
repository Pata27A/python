#generar email
nombre = 'Angel Sanabria'
empresa = 'lincoln'
dominio = 'com.py'


email = f'{nombre}{empresa}@{dominio}'.lower().replace(' ', '')

print(email)