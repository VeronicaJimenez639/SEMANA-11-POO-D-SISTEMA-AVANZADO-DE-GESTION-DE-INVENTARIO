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

        # =====================
        # TABLA (TREEVIEW)
        # =====================
        tabla_frame = ttk.LabelFrame(self.root, text="Listado")
        tabla_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Columnas que se mostrarán
        cols = ("id", "nombre", "cantidad", "precio")
        self.tree = ttk.Treeview(tabla_frame, columns=cols, show="headings", height=14)

        self.tree.heading("id", text="ID")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("precio", text="Precio")

        self.tree.column("id", width=80, anchor="center")
        self.tree.column("nombre", width=360)
        self.tree.column("cantidad", width=120, anchor="center")
        self.tree.column("precio", width=140, anchor="e")

        self.tree.pack(fill="both", expand=True, padx=8, pady=8)

        # Evento: al seleccionar una fila, llenar el formulario
        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

        # Carga inicial de tabla
        self.refrescar_tabla()

        # Evento: al cerrar ventana, guardar
        self.root.protocol("WM_DELETE_WINDOW", self.on_cerrar)

    # =====================
    # CICLO DE VIDA
    # =====================
    def run(self):
        """Inicia el loop de Tkinter (la app se queda escuchando eventos)."""
        self.root.mainloop()

    # =====================
    # UTILIDADES
    # =====================
    def _pintar(self, productos):
        """Pinta una lista de productos en la tabla."""
        # 1) Limpiar filas anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)

        # 2) Insertar filas nuevas
        for p in productos:
            self.tree.insert("", "end", values=(
                p.get_id(),
                p.get_nombre(),
                p.get_cantidad(),
                f"{p.get_precio():.2f}"
            ))

    def refrescar_tabla(self):
        """Muestra todos los productos."""
        self._pintar(self.servicio.productos)

    def leer_formulario(self):
        """Lee y valida datos del formulario.

        - Convierte ID, cantidad y precio a int/float.
        - Valida reglas básicas antes de enviar al servicio.
        """
        try:
            id_p = int(self.var_id.get().strip())
            nombre = self.var_nombre.get().strip()
            cantidad = int(self.var_cantidad.get().strip())
            precio = float(self.var_precio.get().strip())

            if not nombre:
                raise ValueError("Nombre no puede estar vacío")
            if cantidad < 0:
                raise ValueError("Cantidad debe ser >= 0")
            if precio < 0:
                raise ValueError("Precio debe ser >= 0")

            return id_p, nombre, cantidad, precio
        except Exception as e:
            messagebox.showerror("Datos inválidos", f"Revisa el formulario.\nDetalle: {e}")
            return None
        
    def on_limpiar(self):
        """Limpia el formulario y deselecciona la tabla."""
        self.var_id.set("")
        self.var_nombre.set("")
        self.var_cantidad.set("")
        self.var_precio.set("")
        self.tree.selection_remove(self.tree.selection())

    def on_select_row(self, event):
        """Cuando el usuario selecciona una fila, se cargan los datos en el formulario."""
        sel = self.tree.selection()
        if not sel:
            return
        values = self.tree.item(sel[0], "values")
        self.var_id.set(values[0])
        self.var_nombre.set(values[1])
        self.var_cantidad.set(values[2])
        self.var_precio.set(values[3])

    # =====================
    # EVENTOS (CRUD)
    # =====================
    def on_agregar(self):
        """Evento botón Agregar."""
        datos = self.leer_formulario()
        if not datos:
            return
        id_p, nombre, cantidad, precio = datos

        ok, msg = self.servicio.agregar_producto_gui(id_p, nombre, cantidad, precio)
        if ok:
            self.refrescar_tabla()
            self.on_limpiar()
            messagebox.showinfo("OK", msg)
        else:
            messagebox.showwarning("Atención", msg)

    def on_actualizar(self):
        """Evento botón Actualizar."""
        datos = self.leer_formulario()
        if not datos:
            return
        id_p, nombre, cantidad, precio = datos

        ok, msg = self.servicio.actualizar_producto_gui(id_p, cantidad, precio)
        if ok:
            self.refrescar_tabla()
            messagebox.showinfo("OK", msg)
        else:
            messagebox.showwarning("Atención", msg)

    def on_eliminar(self):
        """Evento botón Eliminar."""
        try:
            id_p = int(self.var_id.get().strip())
        except Exception:
            messagebox.showwarning("Atención", "Selecciona un producto (ID) para eliminar.")
            return

        # Confirmación antes de borrar
        if not messagebox.askyesno("Confirmar", f"¿Eliminar el producto ID {id_p}?"):
            return

        ok, msg = self.servicio.eliminar_producto_gui(id_p)
        if ok:
            self.refrescar_tabla()
            self.on_limpiar()
            messagebox.showinfo("OK", msg)
        else:
            messagebox.showwarning("Atención", msg)

    def on_guardar(self):
        """Evento botón Guardar."""
        self.servicio.guardar_en_archivo()
        messagebox.showinfo("Guardado", "Cambios guardados en el archivo.")

    def on_cerrar(self):
        """Al cerrar ventana: guarda y termina la app."""
        self.servicio.guardar_en_archivo()
        self.root.destroy()

    # =====================
    # BÚSQUEDA
    # =====================
    def on_buscar(self):
        """Filtra la tabla por coincidencia parcial de nombre."""
        texto = self.var_buscar.get().strip()
        encontrados = self.servicio.buscar_por_nombre(texto)
        self._pintar(encontrados)

        if texto and not encontrados:
            messagebox.showinfo("Resultado", "No se encontraron productos con ese nombre.")