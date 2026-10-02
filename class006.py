'''
1. Crear una lista con los nombres de los y las clientes que vamos a procesar. Recorrer la lista y mostrar el nombre de cada cliente o clienta, 
junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

2. Recorrer la lista con un for y mostrar el nombre de cada cliente junto con su posición en la lista (por ejemplo: Cliente 1: Ana).

3. Si encontrás un nombre vacío, mostrar un mensaje de alerta indicando que ese dato no es válido.
'''

clientes = ['laura', 'pedro', '', 'maria', '', 'ines']

for indice in range(len(clientes)):
    if clientes[indice] == '':
        print(f'Cliente {indice + 1}: [ALERTA] Nombre no valido.')
    else:
        print(f'Cliente {indice + 1}: {clientes[indice].capitalize()}')


