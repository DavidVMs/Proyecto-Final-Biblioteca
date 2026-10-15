from modelos.libro import Libro
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro_nuevo):
        # buscar si hay otro libro con mismo isbn
        if self.buscar_libro(libro_nuevo):
            print("El libro ya está en la lista")
            return
        self.libros.append(libro_nuevo)
        print("Libro registrado")

    def registrar_usuario(self, usuario_nuevo):
            # buscar si hay otro usuario con mismo id
            if self.buscar_usuario(usuario_nuevo):
                print("El usuario ya está en la lista")
                return
            self.usuarios.append(usuario_nuevo)
            print("Usuario registrado")

    def buscar_libro(self, libro_nuevo):
        for libro in self.libros:
            if libro.__eq__(libro_nuevo):
                return libro
        return None
    
    def buscar_usuario(self, usuario_nuevo):
            for usuario in self.usuarios:
                if usuario.__eq__(usuario_nuevo):
                    return usuario
            return None

    def prestamos_activos(self):
        return [prestamo for prestamo in self.prestamos if prestamo.activo]

    def prestamos_de_usuario(self, usuario):
        return [prestamo for prestamo in self.prestamos if prestamo.usuario == usuario]


            