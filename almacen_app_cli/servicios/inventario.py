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

    # -------- PERSISTENCIA --------
    # Carga los productos desde el archivo
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
                        # Si una línea está dañada, se ignora
                        continue

        except Exception as e:
            print(f"Error al cargar archivo: {e}")

    # Guarda todos los productos actuales en el archivo
    def guardar_en_archivo(self) -> None:
        try:
            self.asegurar_archivo()

            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                for p in self.__productos:
                    f.write(p.to_linea() + "\n")

        except Exception as e:
            print(f"Error al guardar archivo: {e}")

    # -------- CRUD --------
    # Agrega un producto si el ID no existe
    def agregar_producto(self, producto: Producto) -> bool:
        if self._buscar_indice_por_id(producto.get_id()) != -1:
            return False

        self.__productos.append(producto)
        self.guardar_en_archivo()
        return True
    
    # Elimina un producto por ID
    def eliminar_producto(self, producto_id: int) -> bool:
        indice = self._buscar_indice_por_id(producto_id)

        if indice == -1:
            return False

        self.__productos.pop(indice)
        self.guardar_en_archivo()
        return True
    
    # Actualiza cantidad y/o precio
    def actualizar_producto(self, producto_id: int, nueva_cantidad=None, nuevo_precio=None) -> bool:
        indice = self._buscar_indice_por_id(producto_id)

        if indice == -1:
            return False

        producto = self.__productos[indice]

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        self.guardar_en_archivo()
        return True