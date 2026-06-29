# Sistema de Inventario para Tienda Pequeña
# Almacenamiento en diccionario, fácil de adaptar a archivos si lo deseas

# Diccionario principal: clave = código del producto, valor = datos
inventario = {}

def agregar_producto():
    """Agrega un nuevo producto al inventario"""
    codigo = input("Ingrese el código del producto: ").strip()
    if codigo in inventario:
        print("❌ Este código ya existe. Intente con otro.")
        return
    
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        cantidad = int(input("Ingrese la cantidad en stock: "))
        precio = float(input("Ingrese el precio unitario ($): "))
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero y el precio un número válido.")
        return

    inventario[codigo] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
    print(f"✅ Producto '{nombre}' agregado correctamente.")

def ver_inventario():
    """Muestra todos los productos registrados"""
    if not inventario:
        print("📭 El inventario está vacío.")
        return
    
    print("\n" + "="*60)
    print(f"{'CÓDIGO':<10} {'NOMBRE':<25} {'CANTIDAD':<10} {'PRECIO ($)':<12}")
    print("="*60)
    for codigo, datos in inventario.items():
        print(f"{codigo:<10} {datos['nombre']:<25} {datos['cantidad']:<10} {datos['precio']:<12.2f}")
    print("="*60 + "\n")

def actualizar_cantidad():
    """Modifica la cantidad de un producto existente"""
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    if codigo not in inventario:
        print("❌ Producto no encontrado.")
        return
    
    try:
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
        if nueva_cantidad < 0:
            print("❌ La cantidad no puede ser negativa.")
            return
        inventario[codigo]["cantidad"] = nueva_cantidad
        print("✅ Cantidad actualizada correctamente.")
    except ValueError:
        print("❌ Debe ingresar un número entero válido.")

def buscar_producto():
    """Busca un producto por su código"""
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    if codigo in inventario:
        datos = inventario[codigo]
        print("\n🔍 Producto encontrado:")
        print(f"Nombre: {datos['nombre']}")
        print(f"Cantidad en stock: {datos['cantidad']}")
        print(f"Precio unitario: ${datos['precio']:.2f}\n")
    else:
        print("❌ Producto no encontrado.")

def eliminar_producto():
    """Elimina un producto del inventario"""
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    if codigo in inventario:
        nombre = inventario[codigo]["nombre"]
        del inventario[codigo]
        print(f"✅ Producto '{nombre}' eliminado correctamente.")
    else:
        print("❌ Producto no encontrado.")

def menu_principal():
    """Muestra el menú de opciones"""
    while True:
        print("\n" + "="*40)
        print("📋 SISTEMA DE INVENTARIO - TIENDA")
        print("="*40)
        print("1. Agregar producto")
        print("2. Ver todo el inventario")
        print("3. Actualizar cantidad")
        print("4. Buscar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("="*40)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
            buscar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()