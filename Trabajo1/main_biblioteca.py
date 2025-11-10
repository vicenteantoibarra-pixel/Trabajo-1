#Se importan las biblio tecas para poder manipular el codigo
from biblioteca_libros.biblioteca_libors import Biblioteca

library = Biblioteca("Biblioteca Vicente INsano:p")
#Aca se agregan los registros de libros:
library.RegistroLibro("Phantom Blood", "Hirohiko Araki", 10)
library.RegistroLibro("Battle Tendency", "Hirohiko Araki",12)
library.RegistroLibro("Stardust Crusaders", "Hirohiko Araki",35)
library.RegistroLibro("Diamond is Unbreakable", "Hirohiko Araki",6)
library.RegistroLibro("Golden Wind", "Hirohiko Araki",40)
library.RegistroLibro("Stone Ocean", "Hirohiko Araki",10)
library.RegistroLibro("Steel Ball Run", "Hirohiko Araki",40)
library.RegistroLibro("JoJolion", "Hirohiko Araki", 18)

#Esta opcion muestra el catalogo

library.Catalogo()

#Busca de libro por titulo

library.LibroTitulo(input("Ingresa el nombre del libro: "))

#Aca se realiza el prestamo

titulo = input("Ingresa el nombre del libro a seleccionar: ")
cantidad = int(input("Ingresa la cantidad que deseas pedir: "))
library.Prestamo(titulo,cantidad)

#Devolucion de libor

titulo = input("Ingresa el Nombre del libro que quieres devolver: ")
cantidad = int(input("Ingrese la cantidad a devolver: "))
library.Devolucion(titulo,cantidad)

#Catalogo Actualizado

titulo = input("Ingrese el libro que quire ver el catalogo actualizado: ")
library.EstadoActualizado(titulo)