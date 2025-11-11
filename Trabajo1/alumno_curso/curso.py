from alumno_curso.alumno import Alumno
import time
class Curso:
    def __init__(self,nombreCurso):
        self.nombreCurso = nombreCurso
        self.alumnos = []

    def AgregarAlumno (self,nombre):
        nuevo = Alumno(nombre)
        self.alumnos.append(nuevo)
        
    def DeleteAlumno (self,nombre):
        for alumno in self.alumnos: 
            if alumno.nombre == nombre:
                time.sleep(5)
                self.alumnos.remove(alumno)
                print(f"Alumno {nombre} fue eliminado del curso exitosamente")
                return
        print(f"El nombre {nombre} no fue encontrado e el curso")
    
    def List (self):
        if not self.alumnos:
            print("No hay alumnos en este curso")
        else:
            print("El listado de alumnos es el siguiente: ", "\n")
            for alumno in self.alumnos:
                print(f"|Alumno: {alumno.nombre}|")
    
    def EstadoCurso(self):
        estado = f"Curso: {self.nombreCurso}\n"
        estado += "Alumnos inscritos: \n"
        
        if not self.alumnos:
            esatdo += f"|Ninguno|\n"
        else:
            for alumno in self.alumnos:
                estado += f"|{alumno.nombre}|\n"
        return estado            
                   
            
        
