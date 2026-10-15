from modelos.libro import Libro
from modelos.prestamo import Prestamo
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca
from datetime import date

def mostrarMenu():
    print("=========BIBLIOTECA=========")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")
    print("=============================")


def registrar_libro(biblioteca):
    isbn = input("ISBN: ").strip()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = input("Año: ").strip()
    genero = input("Género: ").strip()

    libro = Libro(isbn, titulo, autor, genero, anio)
    biblioteca.registrar_libro(libro)

def registrar_usuario(biblioteca):
    id = input("ID: ").strip()
    nombre = input("Nombre: ").strip()
    apellidos = input("Apellidos: ").strip()
    email = input("Email: ").strip() 

    usuario = Usuario(id, nombre, apellidos, email)
    biblioteca.registrar_usuario(usuario)

def buscar_libro(biblioteca):
    isbn = input("Introduce el ISBN del libro a buscar: ").strip()
    libro_buscado = Libro(isbn, "", "", "")
    libro = biblioteca.buscar_libro(libro_buscado)
    if libro is None:
        print("No se ha encontrado ningún libro con ese ISBN")
    else:
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"Año: {libro.anio}")
        print(f"Género: {libro.genero}")

def listar_libros(biblioteca):
    print ("--Listado de Libros--")    
    for libro in biblioteca.libros:
        print(libro)

def realizar_prestamo(biblioteca):
    isbn = input("Introduce el ISBN del libro: ").strip()
    id_usuario = input("Introduce el ID del usuario al que vas a realizar el préstamo: ").strip()

    libro = biblioteca.buscar_libro(Libro(isbn, "", "", ""))
    usuario = biblioteca.buscar_usuario(Usuario(id_usuario, "", "", ""))

    if libro is None:
        print("ISBN no encontrado")
    elif usuario is None:
        print("ID no encontrado")
    elif not libro.disponible:
        print("Este libro no está disponible")
    else:
        prestamo = Prestamo(usuario, libro)
        biblioteca.prestamos.append(prestamo)
        libro.disponible = False
        print("Préstamo realizado")
        print(prestamo)

def registrar_devolucion(biblioteca):
    isbn = input("Introduce el ISBN del libro que quieras devolver: ").strip()
    libro_buscado = Libro(isbn, "" , "", "")

    for prestamo in biblioteca.prestamos:
        if prestamo.activo and prestamo.libro == libro_buscado:
            prestamo.fecha_devolucion = date.today()
            prestamo.libro.disponible = True
            print("Devolución registrada")
            return
        
    print("No existe ningún préstamo para este ISBN")

def mostrar_prestamos_activos(biblioteca):
    print("--Préstamos activos--")
    activos = biblioteca.prestamos_activos()

    if not activos:
        print("No hay préstamos activos")
        return

    for prestamo in activos:
        print(prestamo)

def mostrar_prestamos_usuario(biblioteca):
    id = input("Introduce el ID del usuario: ").strip()
    usuario = biblioteca.buscar_usuario(Usuario(id,"", "", ""))

    if usuario is None:
        print ("ID de usuario incorrecto")
        return

    prestamos = biblioteca.prestamos_de_usuario(usuario)

    if not prestamos: 
        print("Este usuario no tiene préstamos")
        return
    
    print(f"--Préstamos de {usuario.nombre} {usuario.apellidos}--")

    for prestamo in prestamos:
        print(prestamo)

def main():
    miBiblioteca = Biblioteca()

    while True:
        mostrarMenu()
        try:
            opcion = int(input("Introduce la opción que quieres: "))
        except ValueError:
            print("Opción incorrecta")
            continue

        if opcion == 1:
            registrar_libro(miBiblioteca)
        elif opcion == 2:
            registrar_usuario(miBiblioteca)
        elif opcion == 3:
            buscar_libro(miBiblioteca)
        elif opcion == 4:
            listar_libros(miBiblioteca)
        elif opcion == 5:
            realizar_prestamo(miBiblioteca)
        elif opcion == 6:
            registrar_devolucion(miBiblioteca)
        elif opcion == 7:
            mostrar_prestamos_activos(miBiblioteca)
        elif opcion == 8:
            mostrar_prestamos_usuario(miBiblioteca)
        elif opcion == 9:
            pass
            print("Opción no disponible")
            #Tras consultar como realizar este apartado del ejercicio, he entendido como se realiza todo pero hay cosas que no hemos visto en clase que me gustaría primero tratar en clase.
        elif opcion == 0:
            print("Has salido del programa")
            break 
        else:
            print("Opción incorrecta")   


if __name__ == "__main__":
    main()