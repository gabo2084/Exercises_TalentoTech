
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
email = input('Ingrese su correo: ')

if nombre == '':
    nombre = 'ERROR!'

if apellido == '':
    apellido = 'ERROR!'

if edad < 19:
    edad = 'ERROR!'

if email == '':
    email = 'ERROR!'


print('\n##########################################################')
print('####################  Ficha Personal  ####################')
print('##########################################################\n')

print('Nombre: ', nombre)
print('Apellido: ', apellido)
print('Edad: ', edad)
print('Email: ', email, '\n')