clientes = []

nombre_cliente = ''

while nombre_cliente != 'fin':
    nombre_cliente = input('Ingrese el nombre del cliente(escriba "fin" para salir del programa): ').strip()
    if nombre_cliente.strip().lower() == '' or nombre_cliente.isnumeric():
        print('Nombre no valido. Por favor, vuelva a intentarlo.')
        continue
    elif nombre_cliente.strip().lower() == 'fin':
        print('\nSaliendo del sistema ...')
        break

    clientes.append(nombre_cliente.capitalize())

clientes.sort()

print('\nListado de Clientes\n')

for cliente in clientes:
    
    print(f'- {cliente}')