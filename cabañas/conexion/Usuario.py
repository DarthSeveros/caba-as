from conexion.conexionCRM import conexionCRM

class Usuario():
    def __init__(self):
        self.id_usuario = ""
        self.nombres = ""
        self.apellidos = ""
        self.email = ""
        self.celular = ""
        self.contrasenea = ""
        self.conectado = False
        self.intentos = 3

    def conectar_usuario(self, usuario_ingresado, contra_ingresada):
        usuarios = self.listarUsuario()
        for usuario in usuarios:
            if usuario_ingresado == usuario[0]:
                self.id_usuario = usuario[0]
                self.nombres = usuario[1]
                self.apellidos = usuario[2]
                self.email = usuario[3]
                self.celular = usuario[4]
                self.contrasenea = usuario[5]

            else:
                print("El usuario ingresado no existe")

            while self.intentos > 0:
                if contra_ingresada == usuario[5]:
                    self.conectado = True
                    print("Se ha conectado con exito")
                    break
                else:
                    self.intentos -= 1
                    if self.intentos > 0:
                        print("Contraseña incorrecta, intentelo denuevo")
                        print("Intentos restantes: " + str(self.intentos))
                        contra_ingresada = input("Ingrese su contraseña: ")
                    else:
                        print("Error, no se ha podido iniciar sesión")
            break

        else:
            print("El usuario ingresado no existe")

    def desconectar(self):
        if self.conectado:
            self.conectado = False
            print("Sesión cerrada con exito")

        else:
            print("Error no inicio sesión")

    def __str__(self):
        if self.conectado:
            estado = "Conectado"
        else:
            estado = "Desconectado"
        return "Nombre de usuario: " + str(self.nombres) + "estado: " + str(estado)

    def agregar_usuario(self, id_usuario, nombres, apellidos, email, celular, contrasenea):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        sql = "INSERT INTO usuario (id_usuario, nombres, apellidos, email, celular, contrasenea) VALUES (%s, %s, %s, %s, %s, %s)"

        val = (id_usuario, nombres, apellidos, email, celular, contrasenea)
        cursor.execute(sql, val)
        mydb.commit()

    def listarUsuario(self):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        sql = "SELECT id_usuario, nombres, apellidos, email, celular, contrasenea FROM usuario"
        cursor.execute(sql)
        usuarios1 = cursor.fetchall()
        return usuarios1


    def eliminarUsuario(self, id_usuario):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        # Instrucciones SQL para eliminar
        sql = f"DELETE FROM usuario WHERE id_usuario= '{id_usuario}';"
        cursor.execute(sql)
        mydb.commit()

    def actualizarUsuario(self, id_usuario, nombres, apellidos, email, celular, contrasenea):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        # Instrucciones SQL para actualizar
        sql = "UPDATE FROM usuario SET id_usuario = %s, nombres = %s, apellidos = %s, email = %s, celular = %s, contrasenea = %s"
        val = (id_usuario, nombres, apellidos, email, celular, contrasenea)
        cursor.execute(sql, val)
        mydb.commit()











