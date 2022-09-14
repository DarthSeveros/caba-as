from conexion.conexionCRM import conexionCRM


class Cabaneas():
    def __init__(self):
        self.id_cabaneas = ""
        self.materiales = ""
        self.precio_materiales = ""
        self.cnt_materiales = ""
        self.usuario_id_usuario = ""

    def agregarCabaneas(self, id_cabaneas, materiales, precio_materiales, cnt_materiales):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        sql = "INSERT INTO cabaneas (id_cabaneas, materiales, precio_materiales, usuario_id_usuario, cnt_materiales)" \
              "VALUES (%s, %s, %s, %s, %s)"

        val = (id_cabaneas, materiales, precio_materiales, cnt_materiales)
        cursor.execute(sql, val)
        mydb.commit()

    def listarCabaneas(self):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        # Instrucciones SQL para consultar
        sql = "SELECT id_cabaneas, materiales, precio_materiales, cnt_materiales from cabaneas"

        cursor.execute(sql)
        cabaneas = cursor.fetchall()

        return cabaneas

    def actualizarCabaneas(self, id_cabaneas, materiales, precio_materiales, cnt_materiales):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        # Instrucciones SQL para actualizar
        sql = "UPDATE cabaneas SET id_cabaneas = %s, materiales = %s, precio_materiales = %s, cnt_materiales = %s"
        val = (id_cabaneas, materiales, precio_materiales, cnt_materiales)
        cursor.execute(sql, val)
        mydb.commit()

    def eliminarCabaneas(self):
        obj_conexion = conexionCRM()
        mydb = obj_conexion.abrirConexion()
        cursor = mydb.cursor()

        # Instrucciones SQL para eliminar
        sql = "DELETE FROM cabaneas WHERE id_cabaneas = '{id_cabaneas}';"
        cursor.execute(sql)
        mydb.commit()






