from servicios.restaurante import Restaurante

# 4. TUPLA: Menú fijo que no cambia
MENU: tuple[str,...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir"
)

def main():
    rest = Restaurante()
    while True:
        print("\n========== SISTEMA RESTAURANTE ==========")
        for opcion in MENU:
            print(opcion)
        
        op = input("Seleccione una opción: ")
        
        if op == "1":
            cod = input("Código: ")
            nom = input("Nombre: ")
            cat = input("Categoría: ")
            prec = float(input("Precio: "))
            print(rest.registrar_producto(cod, nom, cat, prec))
        elif op == "2":
            print(rest.buscar_producto(input("Código: ")))
        elif op == "3":
            cod = input("Código: ")
            nom = input("Nuevo nombre: ")
            cat = input("Nueva categoría: ")
            prec = float(input("Nuevo precio: "))
            print(rest.actualizar_producto(cod, nom, cat, prec))
        elif op == "4":
            print(rest.eliminar_producto(input("Código: ")))
        elif op == "5":
            print(rest.listar_productos())
        elif op == "6":
            id_u = input("ID: ")
            nom = input("Nombre: ")
            correo = input("Correo: ")
            print(rest.registrar_usuario(id_u, nom, correo))
        elif op == "7":
            print(rest.listar_usuarios())
        elif op == "8":
            print(rest.mostrar_categorias())
        elif op == "9":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()