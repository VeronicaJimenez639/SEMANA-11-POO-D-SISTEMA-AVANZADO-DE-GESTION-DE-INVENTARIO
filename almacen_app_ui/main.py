# main.py
""" 
Punto de entrada de la aplicación UI.

Aquí solo "conectamos" las capas:
1) Inventario (lógica + archivo)
2) ServicioInventario (adaptador para UI)
3) AppTk (interfaz Tkinter)

main.py no debe tener lógica de negocio.
"""

from servicios.inventario import Inventario
from servicios.servicio_inventario import ServicioInventario
from ui.app_tk import AppTk 