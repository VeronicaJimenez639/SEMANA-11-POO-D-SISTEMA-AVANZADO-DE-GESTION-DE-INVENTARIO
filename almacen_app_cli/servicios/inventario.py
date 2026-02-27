"""
Módulo: inventario.py

Clase Inventario.
Responsable de:
- Gestionar la colección de productos (lista en memoria).
- Ejecutar operaciones CRUD.
- Manejar persistencia en archivo TXT.
"""

import os
from typing import Optional
from modelos.producto import Producto


class Inventario:

    def __init__(self, ruta_archivo: str = None):
        # Lista que almacena los productos en memoria|
        self.__productos: list[Producto] = []

        # Se define la ruta donde se guardará el archivo
        # dirname(dirname(__file__)) permite subir un nivel
        # desde servicios/ hacia almacen_app_cli/
        base_dir = os.path.dirname(os.path.dirname(__file__))

        if ruta_archivo is None:
            ruta_archivo = os.path.join(base_dir, "registros", "inventario.txt")

        self.ruta_archivo = ruta_archivo

        # Al iniciar el programa se cargan los datos guardados
        self.cargar_desde_archivo()