from pelicula_catalogo.pelicula import Pelicula

class Catalogo:
    def __init__(self,cineNombre):
        self.cineNombre = cineNombre
        self.pelicula = []
        
    def RegistrarCatalogo(self,titulo,genero,lanzamiento):
        nombre = Pelicula (titulo,genero,lanzamiento)
        self.pelicula.append(nombre)
    
    def MostrarCatalogo (self):
        for valor in self.pelicula:
            print(f"-- | Pelicula: {valor.titulo}| -- | Genero: {valor.genero} | -- | Fecha lanzamiento: {valor.lanzamiento} | -- ")
        
    def BuscarPelicula(self,titulo):
        for pelicula in self.pelicula:
            if pelicula.titulo == titulo:
                print(f"-- | Pelicula: {pelicula.titulo}| -- | Autor: {pelicula.genero}| -- | Fecha de lanzamiento: {pelicula.lanzamiento} | --") 
                return
            else:
                print("Pelicula no se encuentra en el ctalogo")

    def Genero(self,genero):
        encontrado = False
        for peliculas in self.pelicula:
            if genero in peliculas.genero:
                print(f"-- |titulo: {peliculas.titulo}| -- |Genero: {peliculas.genero}| -- |Fecha de lanzamiendo: {peliculas.lanzamiento}")

            