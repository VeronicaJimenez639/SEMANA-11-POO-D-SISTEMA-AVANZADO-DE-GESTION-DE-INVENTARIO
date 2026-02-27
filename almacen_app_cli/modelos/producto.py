# 1) modelos/producto.py

class Producto:
    """
    Representa un producto del inventario.
    Se encarga de:
    - Validar los datos (ID, nombre, cantidad, precio).
    - Convertirse a texto para guardarse en archivo.
    - Reconstruirse desde una línea del archivo.
    """

    SEPARADOR = "|"  # Formato en TXT: id|nombre|cantidad|precio

    def __init__(self, producto_id: int, nombre: str, cantidad: int, precio: float):
        # Se usan setters para asegurar validación desde la creación del objeto
        self.set_id(producto_id)
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    # -------- Getters (lectura controlada de atributos privados) --------
    def get_id(self) -> int:
        return self.__id      #Retorna el identificador único del producto.

    def get_nombre(self) -> str:
        return self.__nombre    #Retorna el nombre del producto.

    def get_cantidad(self) -> int:
        return self.__cantidad   #Retorna la cantidad disponible.
    
    def get_precio(self) -> float:
        return self.__precio     #Retorna el precio unitario del producto.
    
        # -------- Setters con validación --------
    def set_id(self, producto_id: int) -> None:                    
        if not isinstance(producto_id, int) or producto_id <= 0:   
            raise ValueError("El ID debe ser un entero positivo.")  # Si el ID no es un entero positivo, se lanza una excepción.
        self.__id = producto_id

    def set_nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():   # Si el nombre no es una cadena o está vacía, se lanza una excepción.
            raise ValueError("El nombre no puede estar vacío.")    
        self.__nombre = nombre.strip()

    def set_cantidad(self, cantidad: int) -> None:
        if not isinstance(cantidad, int) or cantidad < 0:       #Asigna la cantidad. Debe ser un entero >= 0.
            raise ValueError("La cantidad debe ser >= 0.")
        self.__cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        if not isinstance(precio, (int, float)) or float(precio) < 0: #Asigna el precio. Debe ser un número >= 0.
            raise ValueError("El precio debe ser >= 0.")
        self.__precio = float(precio)

    # -------- Conversión para persistencia --------
    def to_linea(self) -> str:                                             #Convierte el objeto a una línea de texto para el archivo.
        nombre_seguro = self.get_nombre().replace(self.SEPARADOR, "/")
        return f"{self.get_id()}|{nombre_seguro}|{self.get_cantidad()}|{self.get_precio()}"

    @classmethod
    def from_linea(cls, linea: str) -> "Producto":           #Crea un Producto a partir de una línea del archivo.
        partes = linea.strip().split(cls.SEPARADOR)
        if len(partes) != 4:
            raise ValueError("Línea inválida en archivo.")

        return cls(
            int(partes[0]),
            partes[1],
            int(partes[2]),
            float(partes[3])
        )

    def __str__(self) -> str:             #Representación legible del producto para mostrar en consola.
        return (
            f"ID: {self.get_id()} | "
            f"Nombre: {self.get_nombre()} | "
            f"Cantidad: {self.get_cantidad()} | "
            f"Precio: ${self.get_precio():.2f}"
        )