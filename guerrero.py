from personaje import Personaje 


class Guerrero(Personaje):
   def __init__(self, nombre, nivel, vida,fuerza):
      super().__init__(nombre,nivel,vida)
      self.fuerza = fuerza



   def atacar(self):
      print(f"{self.nombre} realiza un ataque cuerpo a cuerpo con {self.fuerza} de fueza")


   def usar_habilidad(self):
      print(f"{self.nombre} utiliza un ataque especuia con su espada")
      

   
