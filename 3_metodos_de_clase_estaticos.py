class Persona:
    especie= "humano"

    def __init__(self, nombrepersona, edad):
        self.nombre = nombrepersona  # atributo
        self.edad = edad      # atributo

    def saludar(self):
       print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cambiar_especie_a_cada_objeto(self, nueva_especie):
       self.especie = nueva_especie

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18


persona1 = Persona("Ivana", 42)
persona2 = Persona("Pedro", 15)

print(persona1.nombre)
print(persona2.nombre)
print(persona1.especie)
print(persona2.especie)


persona1.cambiar_especie_a_cada_objeto("robot")

Persona.cambiar_especie("humanoide")
print(persona1.especie)
print(persona2.especie)



#print(Persona.es_mayor_de_edad(20))
#print(persona1.es_mayor_de_edad(persona1.edad))
#print(persona2.es_mayor_de_edad(persona2.edad))