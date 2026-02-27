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

# Lee un número decimal (float) y valida mínimo opcional
def leer_float(mensaje: str, minimo=None) -> float:
    """Lee un número decimal (float) desde consola y valida un mínimo opcional."""
    while True:
        try:
            valor = float(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}.")
                continue

            return valor

        except ValueError:
            print("Ingresa un número decimal válido.")

# Lee texto y evita cadenas vacías
def leer_texto(mensaje: str) -> str:
    """Lee un texto no vacío desde consola."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("El texto no puede estar vacío.")

# -----------------------------
# MENÚ PRINCIPAL
# -----------------------------

# Imprime las opciones disponibles para el usuario
def mostrar_menu():
    """Imprime el menú principal del sistema."""
    print("\n" + "=" * 40)
    print("ALMACÉN APP - INVENTARIO")
    print("=" * 40)
    print("1) Añadir producto")
    print("2) Eliminar producto")
    print("3) Actualizar producto")
    print("4) Buscar producto por ID")
    print("5) Buscar producto por nombre")
    print("6) Listar inventario")
    print("7) Salir")

# -----------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------

def main():
    """
    Punto de entrada del programa.

    - Crea una instancia de Inventario.
    - Ejecuta un bucle infinito hasta que el usuario decida salir.
    - Según la opción elegida, llama al método correspondiente.
    """

    # Se crea el inventario (esto carga automáticamente los datos del archivo)
    inventario = Inventario()

    # Bucle principal del sistema
    while True:
        mostrar_menu()
        opcion = leer_int("Elige opción: ", minimo=1)

        # -------- AÑADIR PRODUCTO --------
        if opcion == 1:
            try:
                # Se crea el objeto Producto con datos validados
                producto = Producto(
                    leer_int("ID: ", minimo=1),
                    leer_texto("Nombre: "),
                    leer_int("Cantidad: ", minimo=0),
                    leer_float("Precio: ", minimo=0.0)
                )

                # Se delega la lógica al Inventario
                if inventario.agregar_producto(producto):
                    print("Producto agregado.")
                else:
                    print("El ID ya existe.")

            except ValueError as e:
                # Captura errores de validación del modelo
                print(f"Error: {e}")

        # -------- ELIMINAR PRODUCTO --------
        elif opcion == 2:
            if inventario.eliminar_producto(leer_int("ID: ", minimo=1)):
                print("Producto eliminado.")
            else:
                print("No existe producto con ese ID.")
