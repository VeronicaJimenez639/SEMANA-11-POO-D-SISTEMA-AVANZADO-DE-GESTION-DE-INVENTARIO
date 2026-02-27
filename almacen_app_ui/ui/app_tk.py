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

        # =====================
        # FORMULARIO (ENTRADAS)
        # =====================
        frm = ttk.LabelFrame(self.root, text="Formulario Producto")
        frm.pack(fill="x", padx=10, pady=10)

        # Variables Tkinter (se conectan a los Entry)
        self.var_id = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_cantidad = tk.StringVar()
        self.var_precio = tk.StringVar()

        # Fila 0
        ttk.Label(frm, text="ID").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(frm, textvariable=self.var_id, width=15).grid(row=0, column=1, padx=6, pady=6)

        ttk.Label(frm, text="Nombre").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Entry(frm, textvariable=self.var_nombre, width=30).grid(row=0, column=3, padx=6, pady=6)

        # Fila 1
        ttk.Label(frm, text="Cantidad").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(frm, textvariable=self.var_cantidad, width=15).grid(row=1, column=1, padx=6, pady=6)

        ttk.Label(frm, text="Precio").grid(row=1, column=2, padx=6, pady=6, sticky="w")
        ttk.Entry(frm, textvariable=self.var_precio, width=30).grid(row=1, column=3, padx=6, pady=6)

        # =====================
        # BUSCAR POR NOMBRE
        # =====================
        buscar_frame = ttk.Frame(self.root)
        buscar_frame.pack(fill="x", padx=10, pady=0)

        self.var_buscar = tk.StringVar()
        ttk.Label(buscar_frame, text="Buscar por nombre:").pack(side="left", padx=5)
        ttk.Entry(buscar_frame, textvariable=self.var_buscar, width=35).pack(side="left", padx=5)
        ttk.Button(buscar_frame, text="Buscar", command=self.on_buscar).pack(side="left", padx=5)
        ttk.Button(buscar_frame, text="Ver todo", command=self.refrescar_tabla).pack(side="left", padx=5)

        # =====================
        # BOTONES CRUD
        # =====================
        btns = ttk.Frame(self.root)
        btns.pack(fill="x", padx=10, pady=8)

        ttk.Button(btns, text="Agregar", command=self.on_agregar).pack(side="left", padx=5)
        ttk.Button(btns, text="Actualizar", command=self.on_actualizar).pack(side="left", padx=5)
        ttk.Button(btns, text="Eliminar", command=self.on_eliminar).pack(side="left", padx=5)
        ttk.Button(btns, text="Limpiar", command=self.on_limpiar).pack(side="left", padx=5)
        ttk.Button(btns, text="Guardar", command=self.on_guardar).pack(side="left", padx=5)