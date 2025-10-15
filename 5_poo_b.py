from abc import ABC, abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, propietariocuenta, saldo_inicial):
        self.propietario = propietariocuenta
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def _get_saldo(self):
        return self.__saldo

    def _set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    @abstractmethod
    def retirar(self, valor):
       pass

    def mostrar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"



class CuentaCorriente(CuentaBancaria):  # Herencia
    def retirar(self, valor):
        penalidad = valor * 0.05
        total = valor + penalidad
        if total <= self._get_saldo():
            self._set_saldo(self._get_saldo() - total)
        else:
            print("Fondos insuficientes en la cuenta de ahorro")


class Cuentadeahorros(CuentaBancaria):  # Herencia
    def retirar(self, valor):
        if valor <= self._get_saldo():
            self._set_saldo(self._get_saldo() - valor)
        else:
            print("Fondos insuficientes en la cuenta de nómina")


ccorriente1 = CuentaCorriente("Ricardo", 1000)
cahorro1 = Cuentadeahorros("Pedro", 1000)

ccorriente1.retirar(100)
cahorro1.retirar(100)
print("Cuenta de ahorro: ", ccorriente1.mostrar_saldo())
print("Cuenta de nómina: ", cahorro1.mostrar_saldo())