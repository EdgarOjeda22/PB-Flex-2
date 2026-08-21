
class Jugador:

    def __init__(self,nombre):

        self.nombre = nombre
        self.personaje = None


    def selecccionar_personaje(self, personaje):

        self.personaje = personaje

        print(f"{self.nombre} seleccionó al pj"f"  {personaje.nombre}")
    

    def mostrar_personaje(self):

        if self.personaje is not None:
            print(f"El jugador {self.nombre} "f"utliza a {self.personaje.nombre}")

        else:
            print("El jugador no a seleccionado a ningun personaje")

                  

