
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')
email = input('Ingrese su correo: ')

if nombre == '' or nombre.isnumeric():
    nombre = 'ERROR!'

if apellido == '' or apellido.isnumeric():
    apellido = 'ERROR!'

if not edad.isnumeric():
    edad = 'ERROR'
elif int(edad) < 15:
    edad = 'Niño/Niña'
elif int(edad) >= 15 and int(edad) <= 18:
    edad = 'Adolescente'
else:
    edad = 'Adulto/a'     

if email == '' or email.isnumeric():
    email = 'ERROR!'
elif email.count('@') > 1 or (email.count('@')== 0 and len(email) > 0):
    email = 'Correo invalido.'


print('\n##########################################################')
print('####################  Ficha Personal  ####################')
print('##########################################################\n')

print('Nombre: ', nombre.strip().title())
print('Apellido: ', apellido.strip().title())
print('Rango Etario: ', edad)
print('Email: ', email.strip(), '\n')