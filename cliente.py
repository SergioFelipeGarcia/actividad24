class Cliente:
    #constructor
    def __init__(self,nombre,ciudad,facturacion): #atributos
        self.nombre=nombre
        self.ciudad=ciudad
        self.facturacion=facturacion

cliente1 = Cliente('juan''madrid', 1500)  # instanciar una clase
cliente2 = Cliente('paula''madrid', 1500)  # instanciar una clase
cliente3 = Cliente('javier', 'madrid', 1500)  # instanciar una clase
clientes = [cliente1, cliente2, cliente3]

for cliente in clientes:
    print(cliente)

