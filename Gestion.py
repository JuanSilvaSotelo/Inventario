inventario = {
    'manzanas': 50, 
    'naranjas': 30, 
    'peras': 20
}

def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")

def actualizar_inventario(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad