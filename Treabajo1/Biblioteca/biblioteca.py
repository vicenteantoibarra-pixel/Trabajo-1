class Bliblioteca:
    def __init__(self, nombreBiblioteca, titulo, autor, copiasDispo):
        self.nombreBiblioteca = nombreBiblioteca
        self.titulo = titulo
        self.autor = autor
        self.copiasDispo = copiasDispo
        
    def MostrarCatalogo (self):
        return f"Nombre del libro: ", {self.titulo}, "Nombre del autor: ", {self.autor}, "Copias Disponibles: ", {self.copiasDispo}

    def LibroTitulo (self, libro):
        if libro == self.titulo:
            print (self.titulo, "", self.copiasDispo)
        else: ("Libro no encintrado, ingrese un valor correcto.")

    def Prestamo (self,cantidad):
        self.copiasDispo =- cantidad
        if cantidad + self.copiasDispo:
            print("Losineto no tenemos la cantidad ingresada.")

    def Devolucion (self, devolucion):
        self.copiasDispo =+ devolucion

    def EstadoActualizado (self, Libro1):
        if self.titulo == Libro1:
            print (f"Autro: ",{self.autor}, "Cantidad de este Libro:",{self.copiasDispo})

print ("Hello world!") 