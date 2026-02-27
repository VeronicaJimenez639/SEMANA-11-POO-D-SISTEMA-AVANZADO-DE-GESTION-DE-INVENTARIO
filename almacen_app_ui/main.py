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

def main():
    # 1) Crea inventario (carga productos desde archivo)
    inventario = Inventario()

    # 2) Crea el servicio (puente para la UI)
    servicio = ServicioInventario(inventario)

    # 3) Crea y ejecuta la interfaz
    app = AppTk(servicio)