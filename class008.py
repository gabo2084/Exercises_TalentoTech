
# 1. Crear un diccionario llamado productos donde las claves sean los nombres de los productos y los valores sean sus precios. 

productos = {}

# 2. Permitir que se agreguen productos y sus precios hasta que se decida finalizar.

print('+' * 70)
print(f'{"+" * 25} Lista de productos {"+" * 25}')
print('+' * 70)

deseaContinuar = True

while deseaContinuar:
    
    producto = input("\nIngrese el nombre del producto (o 'salir' para finalizar): ").capitalize().strip()
        
    if producto.lower() == 'salir':
        deseaContinuar = False
        break
    
    elif producto == '' or producto.isnumeric() or producto in productos:
        print("\nNombre de producto inválido o ya existe. Intente nuevamente.")
        continue

    comprobarPrecio = True
    
    while comprobarPrecio:
        
        precio = input("\nIngrese el precio del producto: ").strip()
    
        if not precio or not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
            print("\nPrecio inválido. Intente nuevamente.")
            continue

        comprobarPrecio = False

    productos[producto] = float(precio)

# 3. Mostrar el contenido del diccionario después de cada operación.

    print("\nProductos actuales:\n")
    for nombre, precio in productos.items():
        print(f"- {nombre}: ${precio:.2f}")