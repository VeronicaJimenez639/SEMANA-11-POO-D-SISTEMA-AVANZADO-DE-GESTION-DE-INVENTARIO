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