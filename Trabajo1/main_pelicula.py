from pelicula_catalogo.catalogo import Catalogo

catalogo = Catalogo("Catalogo de peliculas")

catalogo.RegistrarCatalogo("Avatar","Ciencia ficción / Aventura","2009-12-18")
catalogo.RegistrarCatalogo("Avengers: Endgame","Acción / Ciencia ficción","2019-04-26")
catalogo.RegistrarCatalogo("El Padrino","Crimen / Drama","1972-03-24")
catalogo.RegistrarCatalogo("El Señor de los Anillos: La Comunidad del Anillo","Fantasía / Aventura","2001-12-19")
catalogo.RegistrarCatalogo("Forrest Gump","Drama / Romance","1994-07-06")
catalogo.RegistrarCatalogo("Gladiador","Acción / Drama / Histórico","2000-05-05")

catalogo.MostrarCatalogo()

catalogo.BuscarPelicula("Avatar")

catalogo.Genero("Acción")

#me canse de agregar notas:C

