class Cliente:
    def __init__(self, cedula, nombre):
        self._cedula = cedula
        self._nombre = nombre
        self._cuentas = [] 

class Cuenta:
    def __init__(self, numero, tipo, saldo):
        self._numero = numero
        self._tipo = tipo
        self._saldo = saldo

class Banco:
    def __init__(self, nombre):
        self._nombre = nombre
        self._clientes = []

    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def ver_info_clientes(self):
        for cliente in self._clientes:
            print(f"Cédula: {cliente._cedula}, Nombre: {cliente._nombre}")
            for cuenta in cliente._cuentas:
                print(f"  Número de cuenta: {cuenta._numero}, Tipo: {cuenta._tipo}, Saldo: {cuenta._saldo}")

    def total_saldos_ahorros(self):
        total = sum(cuenta._saldo for cliente in self._clientes for cuenta in cliente._cuentas if cuenta._tipo == "ahorros")
        return total

    def total_saldos_corriente(self):
        total = sum(cuenta._saldo for cliente in self._clientes for cuenta in cliente._cuentas if cuenta._tipo == "corriente")
        return total

if __name__ == "__main__":
    banco = Banco("Mi Banco")
    cliente1 = Cliente("123456", "Samuel Bayona")
    cliente2 = Cliente("789012", "Maria Avila")

    cuenta1 = Cuenta("1001", "ahorros", 5000)
    cuenta2 = Cuenta("2001", "corriente", 8000)

    cliente1._cuentas = [cuenta1]
    cliente2._cuentas = [cuenta2]

    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)

    print(f"Nombre del banco: {banco._nombre}")
    print("Información de los clientes:")
    banco.ver_info_clientes()
    print(f"Total de saldos en cuentas de ahorros: {banco.total_saldos_ahorros()}")
    print(f"Total de saldos en cuentas corrientes: {banco.total_saldos_corriente()}")
