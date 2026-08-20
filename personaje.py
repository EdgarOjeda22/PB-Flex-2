

# clase Personaje

class Personaje:
    
    def __init__(self, nombre, edad, vida):
        self.nombre = nombre
        self.edad = edad
        self.vida = vida

    def atacar(self):
        return f"{self.nombre} realiza un ataque."
