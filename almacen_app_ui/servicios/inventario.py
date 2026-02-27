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

    # -------- PERSISTENCIA --------
    def cargar_desde_archivo(self) -> None:
        try:
            self.asegurar_archivo()
            self.__productos.clear()

            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue

                    try:
                        producto = Producto.from_linea(linea)
                        self.__productos.append(producto)
                    except Exception:
                        continue

        except Exception as e:
            print(f"Error al cargar archivo: {e}")

    def guardar_en_archivo(self) -> None:
        try:
            self.asegurar_archivo()
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                for p in self.__productos:
                    f.write(p.to_linea() + "\n")
        except Exception as e:
            print(f"Error al guardar archivo: {e}")