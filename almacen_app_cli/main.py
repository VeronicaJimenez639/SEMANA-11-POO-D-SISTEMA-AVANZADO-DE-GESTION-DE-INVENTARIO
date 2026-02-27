"""
main.py (CLI)

Este módulo representa la capa de presentación en consola.
Su responsabilidad es:
- Mostrar el menú al usuario.
- Solicitar y validar datos de entrada.
- Llamar a los métodos del Inventario.
- Mostrar los resultados en pantalla.

No contiene lógica de negocio, solo interacción con el usuario.
"""

from modelos.producto import Producto
from servicios.inventario import Inventario


# -----------------------------
# FUNCIONES AUXILIARES DE ENTRADA
# -----------------------------

# Lee un número entero y valida que cumpla un mínimo opcional
def leer_int(mensaje: str, minimo=None) -> int:
    """Lee un entero desde consola y valida un mínimo opcional."""
    while True:
        try:
            valor = int(input(mensaje))

            # Validación de mínimo si se especifica
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}.")
                continue

            return valor

        except ValueError:
            print("Ingresa un número entero válido.")