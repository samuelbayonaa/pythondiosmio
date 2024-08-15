class Cliente:
    def __init__(self, cedula, nombre):
        self._cedula = cedula
        self._nombre = nombre

class Banco:
    def __init__(self, nombre):
        self._nombre = nombre
        self._clientes = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self._clientes)

    def obtener_clientes(self):
        return self._clientes

if __name__ == "__main__":
    banco_ejemplo = Banco("Bancolombia")
    cliente1 = Cliente("123456", "SAmuel Bayona")
    cliente2 = Cliente("789012", "María Avila")

    banco_ejemplo.adicionar_cliente(cliente1)
    banco_ejemplo.adicionar_cliente(cliente2)

    print(f"Nombre del banco: {banco_ejemplo._nombre}")
    print(f"Número de clientes: {banco_ejemplo.obtener_numero_clientes()}")
    print("Clientes:")
    for cliente in banco_ejemplo.obtener_clientes():
        print(f"- Cédula: {cliente._cedula}, Nombre: {cliente._nombre}")