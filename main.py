from jugador import Jugador
from mago import Mago 
from objeto import Objeto
from guerrero import Guerrero



def main():
    pass
    #-----------------------
    #-----CREAR JUGADOR-----
    #-------------------------


    nuevo_jugador = Jugador("Edgar")
    jugador2 = ("Carlos")

    #--------------------------
   # -----CREAR PERSONAJE------
   # --------------------------

    mago1 = Mago("Gandalf",12,50,150)
    jugador2 = Guerrero("Kratos",12,12,12)
 

    #-----------------------
    # ASOCIAR JUGADOR CON PJ
    #---------------------- 
    

    nuevo_jugador.selecccionar_personaje(mago1)
    nuevo_jugador.mostrar_personaje()

    nuevo_jugador.selecccionar_personaje(jugador2)
    nuevo_jugador.mostrar_personaje()

    #-----------------------
    # ATAQUE DEL MAGO
    #---------------------- 

    mago1.atacar()
    jugador2.atacar()



    #-----------------------
    # HABILIDAD DEL MAGO
    #----------------------

    mago1.usar_habilidad()
    jugador2.usar_habilidad()


    #-----------------------
    # CREAR OBJETO
    #----------------------

    pocion = Objeto("Poción de vida","Consumible")
    staff = Objeto("Staff del Arcangel","Arma")

    ataque1 = Objeto("doble espada")
    ataque2 = object("Filo doble")
    
    #-----------------------
    # AGREGAR OBJETOS AL INVENTARIO
    #----------------------
    
    
    mago1.inventario.agregar_objetos(pocion)
    mago1.inventario.agregar_objetos(staff)



    #-----------------------
    # MOSTRAR INVENTARIO    
    #----------------------

    mago1.inventario.mostrar_inventario()


    #-----------------------
    # RECIBIR DAÑO
    #----------------------
    

    mago1.recibir_danio(12)






if __name__ =="__main__":
    main()




