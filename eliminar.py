def eliminar_producto(inventario, nombre):
    """Eliminar un producto del inventario."""
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")