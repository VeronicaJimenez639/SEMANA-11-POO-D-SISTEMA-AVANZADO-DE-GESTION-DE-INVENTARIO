# servicios/inventario.py

import os
from typing import Optional
from modelos.producto import Producto


class Inventario:

    def __init__(self, ruta_archivo: str = None):
        self.__productos: list[Producto] = []

        # Guarda en inventario_app_ui/registros/inventario.txt
        base_dir = os.path.dirname(os.path.dirname(__file__))
        if ruta_archivo is None:
            ruta_archivo = os.path.join(base_dir, "registros", "inventario.txt")

        self.ruta_archivo = ruta_archivo
        self.cargar_desde_archivo()

    # -------- INTERNOS --------
    def _buscar_indice_por_id(self, producto_id: int) -> int:
        for i, producto in enumerate(self.__productos):
            if producto.get_id() == producto_id:
                return i
        return -1

    def asegurar_archivo(self) -> None:
        carpeta = os.path.dirname(self.ruta_archivo)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8"):
                pass