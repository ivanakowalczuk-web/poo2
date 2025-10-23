class FondosInsuficientesError(Exception):
    """Excepción personalizada para fondos insuficientes."""
    pass


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        self.saldo += monto
        print(f"✅ Depósito exitoso. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
       if monto > self.saldo:
            raise FondosInsuficientesError("❌ Fondos insuficientes para realizar esta operación.")
        self.saldo -= monto
        print(f"💸 Retiro exitoso. Saldo actual: ${self.saldo}")


# Uso de la clase con manejo de errores
try:
    cuenta = CuentaBancaria("Ivana", 1000)
    cuenta.depositar(500)
    cuenta.retirar(2000)  # Esto genera un error personalizado
except FondosInsuficientesError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
else:
    print("Operaciones realizadas con éxito.")
finally:
    print("🏦 Transacción finalizada.")
