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

    # -------- MÉTODOS INTERNOS --------
    # Busca el índice de un producto por ID
    def _buscar_indice_por_id(self, producto_id: int) -> int:
        for i, producto in enumerate(self.__productos):
            if producto.get_id() == producto_id:
                return i
        return -1

    # Asegura que la carpeta y archivo existan antes de leer/escribir
    def asegurar_archivo(self) -> None:
        carpeta = os.path.dirname(self.ruta_archivo)

        if not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8"):
                pass