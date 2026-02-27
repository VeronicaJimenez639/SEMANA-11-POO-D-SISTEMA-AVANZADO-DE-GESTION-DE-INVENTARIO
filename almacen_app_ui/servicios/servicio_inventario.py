# servicios/servicio_inventario.py
""" 
ServicioInventario (capa de servicio para la UI)

Idea principal:
- Tkinter (UI) trabaja con strings y eventos (clicks, inputs).
- Inventario (lógica) trabaja con objetos Producto y reglas del negocio.

Este archivo actúa como un *adaptador* entre ambos mundos:
- Convierte datos del formulario (strings -> int/float).
- Crea objetos Producto.
- Llama a métodos del Inventario.
- Devuelve (ok, mensaje) para que la UI muestre alerts.

Así la UI no se llena de lógica de negocio y el Inventario no depende de Tkinter.
"""

from modelos.producto import Producto


class ServicioInventario:
    def __init__(self, inventario):
        # inventario es una instancia de la clase Inventario (capa lógica)
        self.inventario = inventario

    @property
    def productos(self):
        """Devuelve la lista actual de productos (copia) para mostrar en la tabla."""
        return self.inventario.listar_productos()
    
    # -----------------
    # MÉTODOS PARA LA UI
    # -----------------

    def agregar_producto_gui(self, producto_id, nombre, cantidad, precio):
        """Agrega un producto desde la UI.

        Recibe datos ya convertidos (id, cantidad int; precio float).
        Devuelve (True/False, mensaje) para que la UI muestre el resultado.
        """
        try:
            p = Producto(producto_id, nombre, cantidad, precio)
            ok = self.inventario.agregar_producto(p)
            return (True, "Producto agregado.") if ok else (False, "El ID ya existe.")
        except Exception as e:
            return False, f"Error: {e}"
        
    def actualizar_producto_gui(self, producto_id, cantidad=None, precio=None):
        """Actualiza cantidad y/o precio de un producto.

        - Si el ID no existe -> ok=False
        - Si los datos son inválidos -> excepción
        """
        try:
            ok = self.inventario.actualizar_producto(producto_id, cantidad, precio)
            return (True, "Producto actualizado.") if ok else (False, "No existe producto con ese ID.")
        except Exception as e:
            return False, f"Error: {e}"