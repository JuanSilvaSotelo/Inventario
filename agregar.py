def agregar_producto(nombre):
    """Agregar un producto a la lista de productos"""
    producto = {"nombre": nombre}
    productos.append(producto)
    print(f"producto '{nombre}' agregado correctamente.")