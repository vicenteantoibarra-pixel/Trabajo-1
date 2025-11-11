class Sensor:
    def __init__(self, nombre_sensor):
        self.nombre = nombre_sensor
        self.valores = []

    def agregar_valor(self, nuevo_valor):
        self.valores.append(nuevo_valor)
        print(f"Se agregó la medición {nuevo_valor} al sensor {self.nombre}.")

    def promedio(self):
        if len(self.valores) == 0:
            print("No hay mediciones registradas para calcular el promedio.")
            return 0
        return round(sum(self.valores) / len(self.valores), 2)

    def valor_maximo(self):
        if len(self.valores) == 0:
            print("No hay mediciones registradas.")
            return None
        return max(self.valores)

    def valor_minimo(self):
        if len(self.valores) == 0:
            print("No hay mediciones registradas.")
            return None
        return min(self.valores)

    def resumen(self):
        print(f"\nResumen del Sensor {self.nombre}")
        if not self.valores:
            print("No existen mediciones para mostrar.")
        else:
            print(f"Cantidad de mediciones: {len(self.valores)}")
            print(f"Promedio: {self.promedio()}")
            print(f"Máximo: {self.valor_maximo()}")
            print(f"Mínimo: {self.valor_minimo()}")

 