from ControlAPP import ControlAPP
from Usuario import Usuario



def mostrar_menu():
    controlApp = ControlAPP()
    usuario1 = Usuario()
    controlApp.conectar()

    print("Seleccione una opcion:")
    opcion = int(input("1) perfil Usuario\n"
                       "2) Perfil Cabañas\n"
                       ": "))

    if opcion == 1:
        print("¿Que desea hacer?")
        opcion = int(input("1) Agregar usuario\n"
                           "2) Listar usuario\n"
                           "3) Actualizar usuario\n"
                           "4) Eliminar usuario\n"
                           "5) Desconectarse\n"
                           ": "))


        if opcion == 1:
            controlApp.agregar_Usuario()
        elif opcion == 2:
            controlApp.listarUsuario()
        elif opcion == 3:
            controlApp.actualizarUsuario()
        elif opcion == 4:
            controlApp.eliminar_Usuario()
        elif opcion == 5:
            controlApp.desconectar(usuario1)
        else:
            print("opcion invalida, intentelo nuevamente")

    elif opcion == 2:
        print("¿Que desea hacer?")
        opcion = int(input("1) Agregar cabaña\n"
                           "2) Listar cabaña\n"
                           "3) Actualizar cabaña\n"
                           "4) Eliminar cabaña\n"
                           "5) Desconectarse\n"
                           ": "))

        if opcion == 1:
            controlApp.agregarCabanea()
        elif opcion == 2:
            controlApp.listarCabanea()
        elif opcion == 3:
            controlApp.actualizarCabanea()
        elif opcion == 4:
            controlApp.eliminarCabanea()
        elif opcion == 5:
            controlApp.desconectar(usuario1)
        else:
            print("opcion invalida, intentelo nuevamente")












