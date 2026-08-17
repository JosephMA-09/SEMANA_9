class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = valor

    def __str__(self) -> str:
        return f"{self.codigo} | {self.nombre} | {self.categoria} | ${self.precio}"