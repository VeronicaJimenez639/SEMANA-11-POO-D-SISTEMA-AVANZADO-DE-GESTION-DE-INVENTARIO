# Sistema Avanzado de Gestión de Inventario
## Programación Orientada a Objetos – Semana 11

---

## Descripción:

Aplicación desarrollada en Python que permite gestionar un inventario de productos mediante:

- Versión por consola (CLI)
- Versión con interfaz gráfica (Tkinter)

El sistema aplica principios de Programación Orientada a Objetos y una arquitectura en capas con separación clara de responsabilidades.

Además, implementa persistencia en archivo, permitiendo conservar los datos incluso después de cerrar la aplicación.

---

## Arquitectura del Proyecto

El proyecto está dividido en dos aplicaciones:
almacen_app_cli: Versión por consola
almacen_app_ui: Versión con interfaz gráfica (Tkinter)



---

## Separación de Capas

### 1️⃣ Modelo (`Producto`)
- Representa la entidad Producto.
- Implementa encapsulamiento con getters y setters.
- Permite convertir el objeto a texto para guardarlo en archivo.
- Permite reconstruir el objeto desde una línea del archivo.

---

### 2️⃣ Lógica de Negocio (`Inventario`)
- Administra la lista de productos.
- Implementa operaciones CRUD:
  - Agregar
  - Actualizar
  - Eliminar
  - Buscar
  - Listar
- Maneja la persistencia en archivo (`inventario.txt`).
- Carga automáticamente los datos al iniciar la aplicación.

---

### 3️⃣ Servicio (`ServicioInventario`)
Actúa como adaptador entre la interfaz gráfica y la lógica del sistema.

- Recibe datos del formulario.
- Convierte tipos (string → int / float).
- Llama a los métodos del Inventario.
- Devuelve resultados en formato `(ok, mensaje)` para que la UI muestre alertas.

Permite mantener la interfaz libre de reglas del negocio.

---

### 4️⃣ Interfaz Gráfica (`AppTk`)
Implementada con Tkinter.

Incluye:

- Formulario de productos
- Tabla (Treeview)
- Botones CRUD
- Búsqueda por nombre
- Confirmación de eliminación
- Guardado automático al cerrar

La UI no contiene lógica de negocio, solo delega al servicio.

---

## 💾 Persistencia de Datos

Los productos se almacenan en: registros/inventario.txt


Formato de cada línea: ID|Nombre|Cantidad|Precio


Al iniciar la aplicación:
- Se verifica que el archivo exista.
- Se cargan automáticamente los productos guardados.

---

## ⚙️ Funcionalidades Implementadas

✔ Agregar producto  
✔ Actualizar producto  
✔ Eliminar producto  
✔ Buscar por nombre (coincidencia parcial)  
✔ Listar productos en tabla  
✔ Validación de datos  
✔ Persistencia en archivo  
✔ Arquitectura en capas  

---

## ▶️ Cómo Ejecutar

###  Versión UI (Tkinter)

Desde la carpeta `almacen_app_ui`:

```bash
python main.py

- Versión CLI

Desde la carpeta almacen_app_cli: python main.py


