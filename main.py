from actualizar_inventario import actualizar_inventario
from mostrar_inventario import mostrar_inventario

inventario = {
    'manzanas': 50, 
    'naranjas': 30, 
    'peras': 20}

print(inventario)
actualizar_inventario(inventario, 'manzanas', -70)
mostrar_inventario(inventario)