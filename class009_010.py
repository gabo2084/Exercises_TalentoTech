
productos = []


def mostrar_menu():
    print("\n" + "+" * 70)
    print(f'{"+" * 25} Menú de opciones {"+" * 25}')
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Eliminar producto")
    print("4. Salir")
    print("+" * 70)


def verificar_nombre_producto(nombre_producto):
    if not nombre_producto or nombre_producto.isnumeric():
        return 'Nombre de producto inválido. Intente nuevamente.'
    return nombre_producto.capitalize().strip()

def verificar_precio_producto(precio_producto):
    if not precio_producto or not precio_producto.replace('.', '', 1).isdigit() or float(precio_producto) <= 0:
        return 'Precio inválido. Intente nuevamente.'
    return float(precio_producto)


def agregar_producto():

    nombre_es_valido = False

    while nombre_es_valido == False:

        nombre_producto = verificar_nombre_producto(input('Ingrese el nombre del producto: '))

        if nombre_producto == 'Nombre de producto inválido. Intente nuevamente.':
            continue
        else:
            nombre_es_valido = True


    precio_es_valido = False

    while precio_es_valido == False:

        precio_producto = verificar_precio_producto(input('Ingrese el precio del producto: '))

        if precio_producto == 'Precio inválido. Intente nuevamente.':
            continue
        else:
            precio_es_valido = True


    producto = {'nombre': nombre_producto, 'precio': precio_producto}

    productos.append(producto)

    print(f'Se agrego el producto: {nombre_producto}')



def consultar_productos():
    if len(productos) == 0:
        print('No hay productos en la lista.')
    else:
        print("\nProductos actuales:\n")
        for producto in productos:
            print(f"- {producto['nombre']}: ${producto['precio']:.2f}")


def eliminar_producto():
    if len(productos) == 0:
        print('No hay productos en la lista.')
    else:
        nombre_producto = input('Ingrese el nombre del producto a eliminar: ').capitalize().strip()
        for producto in productos:
            if producto['nombre'] == nombre_producto:
                productos.remove(producto)
                print(f'Se elimino el producto: {nombre_producto}')
                return

desea_continuar = False

while desea_continuar == False:

    mostrar_menu()

    opcion = input('Seleccione una opción: ')

    if opcion == '4':
        desea_continuar = True
        print('Saliendo del programa...')
        break

    match opcion:
        case '1':
            agregar_producto()
        case '2':
            consultar_productos()
        case '3':
            eliminar_producto()
        case _:
            print('No existe la opcion ingresada. Intente nuevamente.')



