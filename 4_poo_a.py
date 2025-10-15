class CuentaBancaria:
    def __init__(self, propietario, saldo_inicial):
        self.propietario = propietario
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def sacar(self, valor):
        if 0<valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("El monto es mayor al saldo")
    def mostrar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"



cuenta1= CuentaBancaria(propietario="Ivana", saldo_inicial=100)
cuenta1.depositar(500)
cuenta1.sacar(200)
print(cuenta1.mostrar_saldo())