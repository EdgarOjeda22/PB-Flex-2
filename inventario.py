class Inventario:

    def __init__(self):
        self.objetos = []

    def agregar_objetos(self, objeto ):

        self.objetos.append(objeto)

        print(f"{objeto.nombre} ha sido agregado al inventario")

    def mostrar_inventario(self):

        print("\n ---Inventario---")
        # validamos si nuestra lista tiene objetos en el inventario
        if len(self.objetos) == 0:
            print("El inventario está vacio")

        else:
            # recorremos el arreglo de objetos
            for objeto in self.objetos:
                print(f"- {objeto.nombre} ({objeto.tipo})")
