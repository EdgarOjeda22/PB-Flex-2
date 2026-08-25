from jugador import Jugador
from mago import Mago
from guerrero import Guerrero
from objeto import Objeto


#Método principal

def main():
    pass

    # =========
    # CREAR JUGADOR
    # =========

    new_player = Jugador("Eric")
    player_two = Jugador ("Rafael")

    # ========
    # CREAR PJS
    # ========

    magician = Mago("Gandalf", 12, 50, 150) 

    warrior = Guerrero("Aragorn", 10, 100, 80)
    
    # ========
    # ASOCIAR JUGADOR CON PJ
    # ========
    new_player.seleccionar_personaje(magician)

    new_player.mostrar_personaje()

    #JUGADOR 2
    player_two.seleccionar_personaje(warrior)

    player_two.mostrar_personaje()


    # ========
    # ATAQUE DEL MAGO
    # ========
    magician.atacar()

    # ========
    # HABILIDAD DEL MAGO
    # ========
    magician.usar_habilidad()

    # ========
    # CREAR OBJETOS
    # ========
    pocion = Objeto("Poción de vida", "Consumible")
    staff = Objeto("Staff del Arcangel", "Arma")

    # ========
    # Agregar OBJETOS AL INVENTARIO
    # ========
    magician.inventario.agregar_objetos(pocion)
    magician.inventario.agregar_objetos(staff)

    # ========
    # Mostrar Inventario
    # ========
    magician.inventario.mostrar_inventario()  

    # ========
    # RECIBIR DAÑO
    # ========

    magician.recibir_danio(20)


    #ATAQUE
    warrior.atacar()

    #MOSTRAR INFO
    warrior.mostrar_informacion()

    #USAR HABILIDADES Y ATACAR

    warrior.atacar()
    warrior.usar_habilidad()

    #CREAR OBJETOS Y AGREGARLOS INVENTARIO

    escudo = Objeto("Escudo de Hyrule", "escudo")
    espada = Objeto("Excalibur", "arma")

    

if __name__ == "__main__":
    main()
