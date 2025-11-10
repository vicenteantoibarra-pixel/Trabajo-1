class Bliblioteca:
    def __init__(self, nombreBiblioteca):
        self.nombreBiblioteca = nombreBiblioteca
        self.libros = {}
        
        
    def RegistroLibro (self, titulo,autor,copias):
        self.libros[titulo] = Libro(titulo,autor,copias)
        
    def Catalogo (self):
        for libro in self.libos.values():
            print(f"Titulo del libro:", {libro}, "Cantidad: ", {libro.copias})

    def LibroTitulo(self, titulo):
        if titulo in self.libros:
            libro = self.libros[titulo]
            print(f"Título: {libro.titulo} | Autor: {libro.autor} | Copias disponibles: {libro.copias}")
        else:
            print("Libro no encontrado, este libro no se encuentra en el catalogo.")
            
    def Prestamo (self, titulo,):
        if titulo in self.libros:
            libro = self.libros[titulo]
            if libro.copias > 0:
                libro.copias -= 1
                print(f"Se realiza prestamo de libro {titulo}| Las copias que quedan son {libro.copias}" )
            else:
                print(f"No hay copias disposnibles de {titulo}")
        else:
            print("Libor no se encuentra en el catalogo.")        
                
    def Devolucion (self, titulo):
        if titulo in self.libros:
            libro = self.libro[titulo]
            libro.copias += 1
            print(f"Se devolvio un copia correctmante, las copias nuevas son de: {libro.copias}")
        else:
            print("Libro no encontrado en el catalogo.")
                
    def EstadoActualizado (self, titulo):
        if titulo in self.libros:
            libro = self.libro[titulo]
            print(f"El libro es: {libro.titulo},| El autor es : {libro.autor}| Las cantidades son: {libro.copias}")
        else:
            print("Este libro no se encuentra en el catalogo. ")
                
class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
        
        
print ("Hello world!") 