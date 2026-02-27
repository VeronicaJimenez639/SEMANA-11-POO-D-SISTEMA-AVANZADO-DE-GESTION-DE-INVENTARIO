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
