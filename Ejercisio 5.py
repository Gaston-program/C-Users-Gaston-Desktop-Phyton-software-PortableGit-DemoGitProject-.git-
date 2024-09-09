class Biblioteca:
    def __init__(self):
        self.__libros = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.__libros.append(libro)
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Libro")

    def remover_libro(self, titulo):
        for libro in self.__libros:
            if libro.obtener_titulo() == titulo:
                self.__libros.remove(libro)
                return True
        return False

    def mostrar_libros(self):
        if not self.__libros:
            return "No hay libros en la biblioteca."
        lista_libros = []
        for libro in self.__libros:
            lista_libros.append(f"Título: {libro.obtener_titulo()}, Autor: {libro.obtener_autor()}")
        return "\n".join(lista_libros)


class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor



# Ejemplo de uso
if __name__ == "__main__":
    biblio = Biblioteca()

    libro1 = Libro("Piratas del Caribe", "George Orwell")
    libro2 = Libro("Alicia en el pais de las Maravillas", "Aldo Aidar")

    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)

    print("Libros en la biblioteca:")
    print(biblio.mostrar_libros())


