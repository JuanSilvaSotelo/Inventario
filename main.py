from actualizar_inventario import actualizar_inventario
from mostrar_inventario import mostrar_inventario
from agregar import agregar_producto
from eliminar import eliminar_producto

inventario = {
    'manzanas': 50,
    'naranjas': 30,
    'peras': 20}

print("Inventario inicial:")
print(inventario)

print("\nActualizando manzanas (-70)...")
actualizar_inventario(inventario, 'manzanas', -70) # Esto dejará manzanas en -20, quizás quieras validar cantidades negativas?
mostrar_inventario(inventario)

print("\nAgregando kiwis (10)...")
agregar_producto(inventario, 'kiwis', 10)
mostrar_inventario(inventario) # Muestra después de agregar

print("\nEliminando kiwis...")
eliminar_producto(inventario, 'kiwis')
mostrar_inventario(inventario) # Muestra después de eliminar