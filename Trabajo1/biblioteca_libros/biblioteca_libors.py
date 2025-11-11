class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias


class Biblioteca:
    def __init__(self, nombreBiblioteca):
        self.nombreBiblioteca = nombreBiblioteca
        self.libros = {}
        
        
    def RegistroLibro (self, titulo,autor,copias):
        self.libros[titulo] = Libro(titulo,autor,copias)
        
    def Catalogo (self):
        if not self.libros:
            print("No hay libros en el catalogo")
        else:
            print("El catalogo de la Biblioteca es:","\n")
            for libro in self.libros.values():
                print(f"Titulo: {libro.titulo}|Autor: {libro.autor}|Copias disponibles: {libro.copias}")
                
    def LibroTitulo(self, titulo):
        if titulo in self.libros:
            libro = self.libros[titulo]
            print(f"Título: {libro.titulo} | Autor: {libro.autor} | Copias disponibles: {libro.copias}")
        else:
            print("Libro no encontrado, este libro no se encuentra en el catalogo.")
        return
        
    def Prestamo (self, titulo,cantidad):
        if titulo in self.libros:
            libro = self.libros[titulo]
            if libro.copias >= cantidad:
                libro.copias -= cantidad
                print(f"Se realiza prestamo de libro {titulo}| Las copias que quedan son {libro.copias}" )
            else:
                print(f"No hay copias disposnibles de {titulo}")
        else:
            print("Libor no se encuentra en el catalogo.")
            return     
        
            
    def Devolucion (self, Titulo,Cantidad1):
        if Titulo in self.libros:
            libro = self.libros[Titulo]
            libro.copias += Cantidad1
            print(f"Se devolvio un copia correctmante, las copias nuevas son de: {libro.copias}")
        else:
            print("Libro no encontrado en el catalogo.")
            return 

    def EstadoActualizado(self, titulo):
        if titulo in self.libros:
            libro = self.libros[titulo]
            print(f"El libro es: {libro.titulo}, | El autor es : {libro.autor} | Las cantidades son: {libro.copias}")
        else:
            print("Este libro no se encuentra en el catalogo.")


print ("Hello world!") 