# Definir la clase
class Persona:
    def __init__(self, nombrepersona, edad):
        self.nombre = nombrepersona  # atributo
        self.edad = edad      # atributo
    def saludar(self):
       print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


# Crear un objeto (instancia de la clase)
persona1 = Persona("Ivana", 42)

# Usar un método del objeto
persona1.saludar()

# Acceder a los atributos del objeto
print(persona1.nombre)
print(persona1.edad)