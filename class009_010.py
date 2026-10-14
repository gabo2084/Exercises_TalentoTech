
productos = [
    {"nombre": "Laptop", "precio": 1200.50},
    {"nombre": "Mouse", "precio": 15.99},
    {"nombre": "Teclado", "precio": 45.00},
    {"nombre": "Monitor", "precio": 300.00},
    {"nombre": "Auriculares", "precio": 75.50},
    {"nombre": "Webcam", "precio": 55.00},
    {"nombre": "Disco Duro Ssd", "precio": 90.00},
    {"nombre": "Memoria Ram", "precio": 60.00},
    {"nombre": "Cable Hdmi", "precio": 12.50},
    {"nombre": "Soporte Monitor", "precio": 35.00}
]


def mostrar_menu():
    print("\n" + "+" * 70)
    print(f'{"+" * 26} Menú de opciones {"+" * 26}')
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Eliminar producto")
    print("4. Salir")
    print("+" * 70)


def verificar_nombre_producto(nombre_producto):
    if not nombre_producto or nombre_producto.isnumeric():
        return '\nNombre de producto inválido. Intente nuevamente.'
    return nombre_producto.title().strip()

def verificar_precio_producto(precio_producto):
    if not precio_producto or not precio_producto.replace('.', '', 1).isdigit() or float(precio_producto) <= 0:
        return '\nPrecio inválido. Intente nuevamente.'
    return float(precio_producto)


def agregar_producto():

    nombre_es_valido = False

    while nombre_es_valido == False:

        nombre_producto = verificar_nombre_producto(input('\nIngrese el nombre del producto: '))

        if nombre_producto == '\nNombre de producto inválido. Intente nuevamente.':
            continue
        else:
            nombre_es_valido = True


    precio_es_valido = False

    while precio_es_valido == False:

        precio_producto = verificar_precio_producto(input('\nIngrese el precio del producto: '))

        if precio_producto == '\nPrecio inválido. Intente nuevamente.':
            continue
        else:
            precio_es_valido = True


    producto = {'nombre': nombre_producto, 'precio': precio_producto}

    productos.append(producto)

    print(f'\nSe agrego el producto: {nombre_producto}')



def consultar_productos():
    if len(productos) == 0:
        print('\nNo hay productos en la lista.')
    else:
        print("\nProductos actuales:\n")
        for producto in productos:
            print(f"- {producto['nombre']}: ${producto['precio']:.2f}")


def eliminar_producto():
    if len(productos) == 0:
        print('\nNo hay productos en la lista.')
    else:
        consultar_productos()
        
        nombre_producto = input('\nIngrese el nombre del producto a eliminar: ').title().strip()
        for producto in productos:
            if producto['nombre'] == nombre_producto:
                productos.remove(producto)
                print(f'\nSe elimino el producto: {nombre_producto}')
                return

desea_continuar = False

while desea_continuar == False:

    mostrar_menu()

    opcion = input('\nSeleccione una opción: ')

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



