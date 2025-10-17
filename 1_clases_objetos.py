# Definir la clase
class Persona:
    def __init__(self, nombrepersona, edad):
        self.nombre = nombrepersona  # atributo
        self.edad = edad      # atributo
    def saludar(self, saludo):
       print(f"{saludo}, mi nombre es {self.nombre} y tengo {self.edad} años.")


# Crear un objeto (instancia de la clase)
persona1 = Persona("Ivana", 42)

# Usar un método del objeto
persona1.saludar("Hola")

# Acceder a los atributos del objeto
print(f"{persona1.nombre} tiene {persona1.edad} años")
print(persona1.edad)