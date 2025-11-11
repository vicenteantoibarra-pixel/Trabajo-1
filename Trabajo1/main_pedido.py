from pedido_item.pedido import Pedido
#aca se crea un pedido
pedido = Pedido()
#Se agregan los items
pedido.AgregarObjeto("Pan", 1000, 2)
pedido.AgregarObjeto("Leche", 1500, 3)
pedido.AgregarObjeto("Huevos", 200, 12)
#se muestra el listado del carrito
pedido.MostrarListado()
#Total pedido
print(f"\nEl total del pedido es: ${pedido.CalcularTotal()}")
#mostrar estado del pedido
pedido.MostrarEstado()