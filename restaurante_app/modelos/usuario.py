class Usuario:
    def __init__(self, id_usuario: str, nombre: str, correo: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo

    @property
    def correo(self) -> str:
        return self._correo
    
    @correo.setter
    def correo(self, valor: str):
        if "@" not in valor:
            raise ValueError("El correo debe tener @")
        self._correo = valor

    def __str__(self) -> str:
        return f"{self.id_usuario} | {self.nombre} | {self.correo}"