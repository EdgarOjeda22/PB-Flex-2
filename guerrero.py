from personaje import Personaje

class Guerrero(Personaje):

    def __init__(self, nombre, nivel, vida, fuerza):
        super().__init__(nombre, nivel, vida)
        self.fuerza = fuerza
    
        #Polimorfismo
    def atacar(self):
        print(f"{self.nombre} ataca con sus dos espadas"
              f" con {self.fuerza} de fuerza")
        
    def usar_habilidad(self):
         print(f"{self.nombre} utiliza Berserk")
   
