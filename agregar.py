def agregar_producto(inventario, nombre, cantidad):
    """Agregar un producto al inventario o actualizar su cantidad si ya existe."""
    if nombre in inventario:
        inventario[nombre] += cantidad
        print(f"Cantidad de '{nombre}' actualizada a {inventario[nombre]}.")
    else:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")
