def eliminar_producto(nombre):
    """eliminar un producto de la lista de productos"""
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print(f"producto '{nombre}' eliminado correctamente.")
            return
    print(f"producto '{nombre}' no encontrado en la lista.")