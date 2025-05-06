def mostrar_inventario(nombre):
    """mostrar el inventario de un producto"""
    for producto in productos:
        if producto["nombre"] == nombre:
            print(f"inventario de '{nombre}': {producto['inventario']}")
            return
    print(f"producto '{nombre}' no encontrado en la lista.")