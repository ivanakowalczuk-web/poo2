# Definir la clase
class Persona:
    def __init__(self, nombrepersona, edad):
        self.nombre = nombrepersona  # atributo
        self.edad = edad      # atributo
        self._energia = 100
        self.__password= "1234"

    def saludar(self):
       print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def _gastar_energia(self, cantidad):
        self._energia -= cantidad
        return self._energia

    def __generar_password(self):
         return f"{self.nombre}{self.edad}"


# Crear un objeto (instancia de la clase)
persona1 = Persona("Ivana", 42)

# Usar un método del objeto
persona1.saludar()

# Acceder a los atributos del objeto
print(persona1.nombre)
print(persona1.edad)
print(persona1._energia)
print(persona1._Persona__password)
print(persona1._gastar_energia(30))
print(persona1._Persona__generar_password())