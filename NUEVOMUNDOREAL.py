# Sistema de gestión de tienda en línea utilizando POO

# Clase Producto que representa un producto en la tienda
class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto [ID: {self.id_producto}, Nombre: {self.nombre}, Precio: ${self.precio}]"

# Clase ProductoElectronico que hereda de Producto
class ProductoElectronico(Producto):
    def __init__(self, id_producto, nombre, precio, garantia):
        super().__init__(id_producto, nombre, precio)
        self.garantia = garantia

    def __str__(self):
        return f"Producto Electrónico [ID: {self.id_producto}, Nombre: {self.nombre}, Precio: ${self.precio}, Garantía: {self.garantia} años]"

# Clase Cliente que representa un cliente de la tienda
class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Cliente [ID: {self.id_cliente}, Nombre: {self.nombre}, Correo: {self.correo}]"

# Clase Pedido que representa un pedido realizado por un cliente
class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def __str__(self):
        productos_str = ', '.join([str(producto) for producto in self.productos])
        return f"Pedido [ID: {self.id_pedido}, Cliente: {self.cliente.nombre}, Productos: [{productos_str}], Total: ${self.total}]"

# Clase Tienda que gestiona los productos y pedidos
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []
        self.pedidos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_pedido(self, cliente):
        nuevo_pedido = Pedido(len(self.pedidos) + 1, cliente)
        self.pedidos.append(nuevo_pedido)
        return nuevo_pedido

    def __str__(self):
        return f"Tienda {self.nombre} con {len(self.productos)} productos, {len(self.clientes)} clientes y {len(self.pedidos)} pedidos."

# Código principal para demostrar la funcionalidad del sistema

# Crear una tienda
mi_tienda = Tienda("Tienda Online")

# Crear productos
producto1 = Producto(1, "Libro", 12.99)
producto2 = ProductoElectronico(2, "Smartphone", 499.99, 2)

# Agregar productos a la tienda
mi_tienda.agregar_producto(producto1)
mi_tienda.agregar_producto(producto2)

# Crear un cliente
cliente1 = Cliente(1, "Ana Gómez", "ana.gomez@example.com")

# Agregar cliente a la tienda
mi_tienda.agregar_cliente(cliente1)

# Crear un pedido para el cliente
pedido1 = mi_tienda.crear_pedido(cliente1)
pedido1.agregar_producto(producto1)
pedido1.agregar_producto(producto2)

# Mostrar detalles del pedido
print(pedido1)

# Mostrar estado de la tienda
print(mi_tienda)
