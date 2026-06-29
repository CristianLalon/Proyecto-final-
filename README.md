# PROYECTO FINAL 
# MATERIAL LOGICA DE PROGRAMACION
# SISTEMA DE INVENTARIO PARA MI NEGOCIO PROPIO


inventario = [] #Creamos la lista con acceso a los elementos


# Registrar un nuevo producto

def registrar_producto():

    print("\n--- REGISTRAR PRODUCTO ---") 

    nombre = input("Nombre del producto: ").strip()

    # Verificar si ya existe
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("Ese producto ya existe.")
            return

    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto registrado correctamente")



# Mostrar inventario

def mostrar_inventario():

    print("\n------ INVENTARIO DEL LOCAL------")

    if len(inventario) == 0:
        print("No existen productos.")
        return

    print("{:<20}{:<12}{:<10}".format(
        "Producto", "Precio", "Cantidad"))

    print("-"*42)

    for producto in inventario:

        print("{:<20}${:<11.2f}{:<10}".format(
            producto["nombre"],
            producto["precio"],
            producto["cantidad"]
        ))



# Buscar producto

def buscar_producto():

    nombre = input("\nIngrese el nombre: ")

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            print("\nProducto encontrado")

            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Cantidad:", producto["cantidad"])

            return

    print("Producto no encontrado.")



# Actualizar cantidad

def actualizar_cantidad():

    nombre = input("\nProducto: ")

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            nueva = int(input("Nueva cantidad: "))

            producto["cantidad"] = nueva

            print("Cantidad actualizada.")

            return

    print("Producto no encontrado.")



# Eliminar producto

def eliminar_producto():

    nombre = input("\nProducto a eliminar: ")

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            inventario.remove(producto)

            print("Producto eliminado.")

            return

    print("Producto no encontrado.")



# Registrar venta

def vender_producto():

    nombre = input("\nProducto vendido: ")

    for producto in inventario:

        if producto["nombre"].lower() == nombre.lower():

            cantidad = int(input("Cantidad vendida: "))

            if cantidad <= producto["cantidad"]:

                producto["cantidad"] -= cantidad

                total = cantidad * producto["precio"]

                print("Venta realizada.")

                print("Total: $", round(total, 2))

            else:

                print("No hay suficiente stock.")

            return

    print("Producto no encontrado.")



# Productos con poco stock

def stock_bajo():

    print("\n--- PRODUCTOS CON STOCK BAJO SON LOS SIGUIENTES ---")

    encontrado = False

    for producto in inventario:

        if producto["cantidad"] < 5:

            encontrado = True

            print(producto["nombre"],
                  "- Cantidad:",
                  producto["cantidad"])

    if not encontrado:
        print("Todos los productos tienen suficiente stock.")



# Valor del inventario

def valor_inventario():

    total = 0

    for producto in inventario:

        total += producto["precio"] * producto["cantidad"]

    print("\nValor total del inventario: $", round(total, 2))



# MENÚ QUE SE MUESTRA AL USUARIO DEL PROGRAMA

while True:

    print("\n ___________________________________")
    print("|         COMERCIAL JEVETCYS        |")
    print("|       SISTEMA DE INVENTARIO       |")
    print("|  Duran-Guayas                     |")
    print("|___________________________________|")
    print("| Menu principal                    |")
    print("| 1. Registrar producto             |")
    print("| 2. Mostrar inventario             |")
    print("| 3. Buscar producto                |")
    print("| 4. Actualizar cantidad            |")
    print("| 5. Eliminar producto              |")
    print("| 6. Registrar venta                |")
    print("| 7. Productos con stock bajo       |")
    print("| 8. Valor total del inventario     |")
    print("| 9. Salir                          |")
    print("|___________________________________|")

    opcion = input("Seleccione una opción: ")

    if opcion == "1": # Centencia para que el usuario oueda elegir una opcion
        registrar_producto()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        actualizar_cantidad()

    elif opcion == "5":
        eliminar_producto()

    elif opcion == "6":
        vender_producto()

    elif opcion == "7":
        stock_bajo()

    elif opcion == "8":
        valor_inventario()

    elif opcion == "9": # Bucle termina si el usuario elije la opcion 9

        print("\nGracias por utilizar el sistema.")

        break

    else:   # Caso donde el usuario elije una opcion que no esta dentro del rango
        print("Opción incorrecta.")
