import json
import os


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id} - {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_en_archivo()
            print("✅ Producto eliminado")
        else:
            print("⚠️ No existe un producto con ese ID")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_en_archivo()
            print("✅ Producto actualizado")
        else:
            print("⚠️ No existe un producto con ese ID")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("⚠️ No se encontró un producto con ese nombre")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("📦 El inventario está vacío")

    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            json.dump({id: vars(p) for id, p in self.productos.items()}, f, indent=4)

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                try:
                    data = json.load(f)
                    self.productos = {id: Producto(**info) for id, info in data.items()}
                except json.JSONDecodeError:
                    self.productos = {}
        else:
            self.productos = {}


def menu():
    inventario = Inventario()

    while True:
        print("\n📌 Menú de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío si no cambias): ")
            precio = input("Nuevo precio (deja vacío si no cambias): ")
            inventario.actualizar_producto(id,
                                           int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
