from conexion.Cabaneas import Cabaneas
from conexion.Usuario import Usuario

class ControlAPP:
    def conectar(self):
        usuario_ingresado = input("Ingrese su nombre de usuario: ")
        contra_ingresada = input("Ingrese su contraseña: ")
        usuario1 = Usuario()
        usuario1.conectar_usuario(usuario_ingresado, contra_ingresada)

    def desconectar(self, usuario1):
        usuario1.desconectar()

    def agregar_Usuario(self):
        usuario1 = Usuario()
        id_usuario = input("Ingrese rut de usuario: ")
        nombres = input("Ingrese nombre de usuario (sin apellido): ")
        apellidos = input("Ingrese apellido: ")
        email = input("Ingrese email de usuario: ")
        celular = input("Ingrese número de celular")
        contrasenea = input("Ingrese contraseña: ")

        usuario1.agregar_usuario(id_usuario, nombres, apellidos, email, celular, contrasenea)

    def eliminar_Usuario(self):
        usuario1 = Usuario()

        id_usuario = input("Ingrese rut de usuario que desea eliminar: ")
        usuario1.eliminarUsuario(id_usuario)
        print("Registro eliminado")

    def listarUsuario(self):
        usuarios = Usuario()
        usuario1 = usuarios.listarUsuario()

        for usuario in usuario1:
            print("Rut : " + usuario[0])
            print("Nombre : " + usuario[1])
            print("Apellido : " + usuario[2])
            print("Email : " + usuario[3])
            #print("Celular : " + usuario[4])
            print("contraseña : " + usuario[5])

    def actualizarUsuario(self):
        id_cliente = input("Ingrese rut de usuario: ")
        nombres = input("Ingrese nombre: ")
        apellidos = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        celular = int(input("Ingrese numero de celular: "))
        contrasenea = input("Ingrese contraeña: ")

        obj_usuario = Usuario()
        obj_usuario.actualizarUsuario(id_cliente, nombres, apellidos, email, celular, contrasenea)

    def agregarCabanea(self):
        cabanea1 = Cabaneas()
        materiales = ""
        conteo_material = 0
        suma_total = 0
        precio_materiales = ""
        id_cabaneas = int(input("Ingrese el numero de la cabaña: "))
        cnt_materiales = int(input("Ingrese la cantidad total de materiales a utilizar: "))

        for x in range(cnt_materiales):
            if conteo_material < cnt_materiales:
                # ingreso de datos
                nombre_material = input("Ingrese el nombre del material a utilizar: ")
                materiales = materiales + nombre_material
                precio_materiales = int(input("Ingrese precio del producto: $"))
                suma_total = suma_total + precio_materiales
                conteo_material = conteo_material + 1


            else:
                print("datos ingresados correctamente")

        cabanea1.agregarCabaneas(id_cabaneas, materiales, precio_materiales, cnt_materiales)

    def actualizarCabanea(self):
        id_cabaneas = input("Ingrese numero de cabaña: ")
        materiales = input("Ingrese nombre de material: ")
        precio_materiales = input("Ingrese precio de material: ")
        cnt_materiales = input("Ingrese cantidad de materiales en total: ")

        obj_cabanea = Cabaneas()
        obj_cabanea.actualizarCabaneas(id_cabaneas, materiales, precio_materiales, cnt_materiales)

    def eliminarCabanea(self):
        cabanea1 = Cabaneas()

        id_cabaneas = input("Ingrese el numero de la cabaña que desea eliminar: ")
        cabanea1.eliminarCabaneas(id_cabaneas)
        print("Cabaña eliminada con exito")

    def listarCabanea(self):
        cabaneas = Cabaneas()
        cabanea1 = cabaneas.listarCabaneas()

        for cabaneas in cabanea1:
            print("numero de cabaña : " + cabaneas[0])
            print("Materiales de cabaña " + cabaneas[0] + ": " + cabaneas[1])
            print("precio de materiales cabaña " + cabaneas[0] + ": " + cabaneas[2])
            print("Cantidad de materiales usados en cabaña " + cabaneas[0] + ": " + cabaneas[5])
            print("Total costo de cabaña " + cabaneas[0] + ": " + cabaneas[4])







