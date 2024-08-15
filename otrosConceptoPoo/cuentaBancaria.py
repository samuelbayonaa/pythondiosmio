class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial, moneda):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__moneda = moneda

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad a retirar inválida.")

    def transferir(self, cuenta_destino, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo and self.__moneda == cuenta_destino.obtener_moneda():
            self.retirar(cantidad)
            cuenta_destino.depositar(cantidad)
        else:
            print("Transferencia no permitida. Verifique fondos, cantidad o moneda.")

    def obtener_saldo(self):
        return self.__saldo

    def obtener_titular(self):
        return self.__titular

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    def obtener_moneda(self):
        return self.__moneda

if __name__ == "__main__":
    cuenta1 = CuentaBancaria("12345", "Samuel Bayona", 1000, "COP")
    cuenta2 = CuentaBancaria("67890", "Maria Avila", 500, "USD")

    cuenta1.depositar(500)

    try:
        cuenta1.transferir(cuenta2, 200)
    except AttributeError:
        print("Error: Las cuentas deben tener la misma moneda para realizar transferencias.")

    cuenta3 = CuentaBancaria("90123", "James Rodriguez", 800, "COP")  
    cuenta1.transferir(cuenta3, 300)

    print("Saldo de la cuenta 1:", cuenta1.obtener_saldo())
    print("Saldo de la cuenta 2:", cuenta2.obtener_saldo())
    print("Saldo de la cuenta 3:", cuenta3.obtener_saldo())
