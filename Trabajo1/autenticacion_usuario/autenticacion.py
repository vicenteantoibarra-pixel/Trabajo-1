from autenticacion_usuario.usuario import Usuario


class Autenticacion:
    def __init__(self):
        self.usuarios = {}
    
    def Registrar(self, nombreUsuario, contraseña):
        if nombreUsuario in self.usuarios:
            print(f"Registro fallido: el usuario '{nombreUsuario}' ya existe.")
            return False
        nuevo = Usuario(nombreUsuario, contraseña)
        self.usuarios[nombreUsuario] = nuevo
        print(f"Registro exitoso: usuario '{nombreUsuario}' creado.")
        return True

    def usuario_registrado(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            print(f"El usuario '{nombre_usuario}' esta registrado.")
            return True
        else:
            print(f"El usuario '{nombre_usuario}' No esta registrado.")
            return False

    def login(self, nombreUsuario, contraseña):
        if nombreUsuario not in self.usuarios:
            print(f"Acceso rechazado: el usuario '{nombreUsuario}' no existe.")
            return False
        
        usuario = self.usuarios[nombreUsuario]

        if usuario.contraseña == contraseña:
            print(f"Acceso autorizado: bienvenido , '{nombreUsuario}'.")
            return True
        else:
            print("Acceso rechazado: contraseña incorrecta.")
            return False

        
        
        