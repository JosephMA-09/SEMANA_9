from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self):
        # 1. LISTA: para guardar y listar todo
        self.productos_lista: list[Producto] = []
        self.usuarios_lista: list[Usuario] = []
        
        # 2. DICCIONARIO: para buscar rápido y validar duplicados
        self.productos_dict: dict[str, Producto] = {}
        self.usuarios_dict: dict[str, Usuario] = {}
        
        # 3. CONJUNTO: para guardar categorías sin repetir
        self.categorias: set[str] = set()

    # --- CRUD PRODUCTOS ---
    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> str:
        if codigo in self.productos_dict:
            return "Error: El código ya existe"
        try:
            p = Producto(codigo, nombre, categoria, precio)
        except ValueError as e:
            return f"Error: {e}"
        self.productos_lista.append(p) # LISTA
        self.productos_dict[codigo] = p # DICCIONARIO
        self.categorias.add(categoria) # CONJUNTO
        return "Producto registrado con éxito"

    def listar_productos(self) -> str:
        if not self.productos_lista:
            return "No hay productos registrados"
        return "\n".join(str(p) for p in self.productos_lista)

    def buscar_producto(self, codigo: str) -> str:
        p = self.productos_dict.get(codigo)
        return str(p) if p else "Producto no encontrado"

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float) -> str:
        if codigo not in self.productos_dict:
            return "Producto no encontrado"
        try:
            p = self.productos_dict[codigo]
            p.nombre = nombre
            p.categoria = categoria
            p.precio = precio
            self.categorias.add(categoria)
            return "Producto actualizado"
        except ValueError as e:
            return f"Error: {e}"

    def eliminar_producto(self, codigo: str) -> str:
        if codigo not in self.productos_dict:
            return "Producto no encontrado"
        p = self.productos_dict.pop(codigo) # DICCIONARIO
        self.productos_lista.remove(p) # LISTA
        return "Producto eliminado"

    # --- CRUD USUARIOS ---
    def registrar_usuario(self, id_usuario: str, nombre: str, correo: str) -> str:
        if id_usuario in self.usuarios_dict:
            return "Error: ID ya existe"
        try:
            u = Usuario(id_usuario, nombre, correo)
        except ValueError as e:
            return f"Error: {e}"
        self.usuarios_lista.append(u)
        self.usuarios_dict[id_usuario] = u
        return "Usuario registrado"

    def listar_usuarios(self) -> str:
        if not self.usuarios_lista:
            return "No hay usuarios registrados"
        return "\n".join(str(u) for u in self.usuarios_lista)

    def mostrar_categorias(self) -> str:
        return f"Categorías: {', '.join(self.categorias)}" if self.categorias else "No hay categorías"