
from alumno_curso.curso import Curso
#Se crea nombre del curso 
curso = Curso("Curso F")
#Se agrgan alumnos al curso
curso.AgregarAlumno("Carlos")
curso.AgregarAlumno("Maria")
curso.AgregarAlumno("Vicente")
curso.AgregarAlumno("Juan")
curso.AgregarAlumno("Fernanda")
curso.AgregarAlumno("Florencia")
#Delete alumno
nombre = input("Ingrese el nombre del estudiante a cual borrar:")
curso.DeleteAlumno = nombre
#lista de alumnos 
curso.List()
#Estado del curso 
curso.EstadoCurso()



