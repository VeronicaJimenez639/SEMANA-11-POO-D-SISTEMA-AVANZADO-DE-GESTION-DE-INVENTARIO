# ui/app_tk.py
"""
AppTk (Tkinter)

Esta clase construye la interfaz gráfica:
- Formulario para ingresar/editar productos.
- Botones para acciones CRUD.
- Tabla (Treeview) para mostrar los productos.
- Búsqueda por nombre.

Regla de oro:
- La UI NO implementa la lógica del inventario.
- La UI delega al 'servicio' (ServicioInventario).

Así mantenemos separación de capas: UI -> Servicio -> Inventario -> Archivo.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class AppTk:
    def __init__(self, servicio):
        # ServicioInventario: puente entre la UI y la lógica
        self.servicio = servicio

        # Ventana principal
        self.root = tk.Tk()
        self.root.title("Inventario (Tkinter)")
        self.root.geometry("920x560")