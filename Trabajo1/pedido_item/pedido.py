# Diseñe un sistema sencillo para gestionar un pedido de compra. Cada ítem del pedido debe tener un
# nombre, un precio y una cantidad, y debe ser capaz de calcular su propio subtotal (precio por cantidad).
# El pedido debe permitir registrar varios ítems y ofrecer una forma de calcular el monto total a pagar
# sumando los subtotales de todos los ítems incluidos.
# • El sistema debe permitir registrar un nuevo ítem indicando su nombre, precio y cantidad.
# • El sistema debe permitir calcular el subtotal de un ítem, multiplicando su precio por la cantidad.
# • El sistema debe permitir agregar ítems a un pedido, de modo que un mismo pedido pueda
# contener varios ítems distintos.
# • El sistema debe permitir consultar el listado de ítems de un pedido, mostrando al menos el
# nombre, el precio, la cantidad y el subtotal de cada uno.
# • El sistema debe permitir calcular el total del pedido, sumando los subtotales de todos los ítems
# registrados.
# • El sistema debe ofrecer una forma de visualizar el total final a pagar junto con el detalle de los
# ítems que lo componen
from pedido_item.item import Item
class Pedido:
    def __init__(self):
        self.items = {}
    
    def AgregarObjeto (self,nombre,precio,cantidad):
        self.items[nombre] = Item (nombre,precio,cantidad)
        
    
    def MostrarListado(self):
        if not self.items:
            print("No hay items en el carrito")
        else:
            print("Lo que tienes en el carrito es:\n")
            for item in self.items.values():
                print(f"[{item.nombre}: ${item.precio} x {item.cantidad} = {item.calcular_subtotal()}]")
    
    def CalcularTotal (self):
        if not self.items:
            print("No hay Items en el pedido")
            return 0
        total = 0
        for item in self.items.values():
            total += item.calcular_subtotal()
        return total
       
    def MostrarEstado(self):
        if not self.items:
            print("El pedido está vacío.")
        else:
            print("\nDetalle del pedido:")
            for item in self.items.values():
                print(f"|{item.nombre}: ${item.precio} x {item.cantidad} = {item.calcular_subtotal()}")
            print(f"TOTAL A PAGAR: ${self.CalcularTotal()}")
                
            
    
    
    
    
    