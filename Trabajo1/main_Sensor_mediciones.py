from sensor_mediciones.sensor import Sensor

#Se le agrega un nombre al sensor
sensor_humedad = Sensor("Sensor de Humedad")

# Se registran valores
sensor_humedad.agregar_valor(45.2)
sensor_humedad.agregar_valor(47.8)
sensor_humedad.agregar_valor(50.1)
sensor_humedad.agregar_valor(46.5)

#se muestra resumen
sensor_humedad.resumen()

#consulta de valores
print("\nConsultas individuales:")
print(f"Promedio: {sensor_humedad.promedio()}")
print(f"Máximo: {sensor_humedad.valor_maximo()}")
print(f"Mínimo: {sensor_humedad.valor_minimo()}")