from agenda_contacto.contacto import Contacto

class Agenda:
    def __init__(self):
        # Diccionario: clave = nombre del contacto, valor = objeto Contacto
        self.contactos = {}

    # 1️⃣ Agregar contacto
    def agregarContacto(self, nombre, telefono, correo):
        if nombre in self.contactos:
            print(f"El contacto {nombre} ya existe en la agenda.")
        else:
            self.contactos[nombre] = Contacto(nombre, telefono, correo)
            print(f"Contacto {nombre} agregado exitosamente.")
        self.mostrarAgenda()

    # 2️⃣ Listar contactos
    def listarContactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("\nCONTACTOS REGISTRADOS:")
            for contacto in self.contactos.values():
                print(contacto)

    # 3️⃣ Buscar contacto
    def buscarContacto(self, nombre):
        if nombre in self.contactos:
            print(f"\nContacto encontrado:\n{self.contactos[nombre]}")
        else:
            print(f"No se encontró ningún contacto con el nombre {nombre}.")
        self.mostrarAgenda()

    def eliminarContacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"🗑 Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"No se puede eliminar: el contacto '{nombre}' no existe.")
        self.mostrarAgenda()

    def mostrarAgenda(self):
        print("\nEstado actual de la agenda:")
        self.listarContactos()