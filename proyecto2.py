import os

class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id} | {self.nombre:<20} | Precio: ${self.precio:>6.2f} | Stock: {self.stock:>4}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"⚠️ El ID {producto.id} ya existe. Use la opción de actualizar stock.")
            return False
        self.productos[producto.id] = producto
        return True

    def actualizar_stock(self, id_producto, nuevo_stock):
        if id_producto in self.productos:
            self.productos[id_producto].stock = nuevo_stock
            return True
        return False

    def buscar_producto(self, id_producto):
        return self.productos.get(id_producto, None)

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\n" + "="*55)
        print(f"{'INVENTARIO DE LA TIENDA':^55}")
        print("="*55)
        for prod in self.productos.values():
            print(prod)
        print("="*55)


class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.cargar_datos_prueba() # Opcional: para no empezar con la tienda vacía

    def cargar_datos_prueba(self):
        # Productos iniciales para probar el sistema de inmediato
        self.inventario.agregar_producto(Producto("101", "Arroz (1kg)", 1.50, 50))
        self.inventario.agregar_producto(Producto("102", "Aceite de cocina", 3.20, 20))
        self.inventario.agregar_producto(Producto("103", "Leche (1L)", 1.10, 30))
        self.inventario.agregar_producto(Producto("104", "Café (250g)", 4.50, 15))

    def realizar_venta(self):
        carrito = []
        self.inventario.mostrar_inventario()
        
        print("\n--- Modo Venta (Escriba 'fin' para terminar) ---")
        while True:
            id_prod = input("Ingrese el ID del producto a vender: ").strip()
            if id_prod.lower() == 'fin':
                break
                
            producto = self.inventario.buscar_producto(id_prod)
            if not producto:
                print("❌ Producto no encontrado.")
                continue
                
            if producto.stock == 0:
                print(f"❌ No hay stock disponible de {producto.nombre}.")
                continue
                
            try:
                cantidad = int(input(f"Cantidad de '{producto.nombre}' (Stock actual: {producto.stock}): "))
                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a cero.")
                    continue
                if cantidad > producto.stock:
                    print(f"⚠️ Stock insuficiente. Solo quedan {producto.stock} unidades.")
                    continue
            except ValueError:
                print("⚠️ Por favor, ingrese un número entero válido.")
                continue

            # Descontar temporalmente del stock y añadir al carrito
            producto.stock -= cantidad
            carrito.append({"producto": producto, "cantidad": cantidad})
            print(f"✅ Añadido: {cantidad} x {producto.nombre}")

        if not carrito:
            print("Venta cancelada (carrito vacío).")
            return

        # Generar Factura
        self.generar_factura(carrito)

    def generar_factura(self, carrito):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "*"*40)
        print(f"{'TICKET DE VENTA':^40}")
        print("*"*40)
        total = 0
        for item in carrito:
            p = item["producto"]
            cant = item["cantidad"]
            subtotal = p.precio * cant
            total += subtotal
            print(f"{cant}x {p.nombre:<20} | ${subtotal:>6.2f}")
        print("-"*40)
        print(f"{'TOTAL A PAGAR:':<30} ${total:>6.2f}")
        print("*"*40)
        print(f"{'¡Gracias por su compra!':^40}\n")


# --- MENÚ INTERACTIVO PRINCIPAL ---
def menu():
    tienda = Tienda()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE TIENDA ===")
        print("1. Ver Inventario")
        print("2. Registrar Nueva Venta")
        print("3. Agregar Nuevo Producto al Inventario")
        print("4. Actualizar Stock de un Producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            tienda.inventario.mostrar_inventario()
        elif opcion == "2":
            tienda.realizar_venta()
        elif opcion == "3":
            print("\n--- Registrar Producto ---")
            id_p = input("ID único del producto: ").strip()
            nom = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio: $"))
                stock = int(input("Stock inicial: "))
                if precio < 0 or stock < 0:
                    print("⚠️ El precio y el stock no pueden ser negativos.")
                    continue
                nuevo_prod = Producto(id_p, nom, precio, stock)
                if tienda.inventario.agregar_producto(nuevo_prod):
                    print("✅ Producto agregado con éxito.")
            except ValueError:
                print("❌ Datos inválidos. El precio debe ser decimal y el stock entero.")
        elif opcion == "4":
            print("\n--- Actualizar Stock ---")
            id_p = input("ID del producto: ").strip()
            try:
                nuevo_st = int(input("Nuevo stock total: "))
                if nuevo_st < 0:
                    print("⚠️ El stock no puede ser negativo.")
                    continue
                if tienda.inventario.actualizar_stock(id_p, nuevo_st):
                    print("✅ Stock actualizado con éxito.")
                else:
                    print("❌ Producto no encontrado.")
            except ValueError:
                print("❌ El stock debe ser un número entero.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()