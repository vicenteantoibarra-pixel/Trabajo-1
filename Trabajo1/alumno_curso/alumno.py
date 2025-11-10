# Diseñe un sistema sencillo para gestionar la inscripción de alumnos en un curso. Cada alumno debe
# estar identificado por su nombre. El curso debe tener un nombre y mantener el listado de alumnos
# inscritos, permitiendo agregar nuevos alumnos, retirar alumnos existentes y consultar en cualquier
# momento quiénes forman parte del curso.
# • El sistema debe permitir definir un nuevo curso, indicando su nombre.
# • El sistema debe permitir registrar un nuevo alumno, indicando su nombre, y inscribirlo en el
# curso.
# • El sistema debe permitir remover a un alumno del curso, de modo que ya no aparezca en el
# listado de inscritos.
# • El sistema debe permitir listar todos los alumnos inscritos en el curso, mostrando al menos su
# nombre.
# • Si se intenta remover a un alumno que no está inscrito, el sistema debe informarlo claramente.
# • El sistema debe ofrecer una forma de consultar el estado actualizado del curso, es decir, su
# nombre y el listado actual de alumnos inscritos

class Alumno:
    def __init__(self,nombre, apellido, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        
        