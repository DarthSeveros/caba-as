
class conexionCRM:
    def __init__(self):
        self.servidor = "localhost"
        self.usuario = "root"
        self.clave = "12345"
        self.basedatos = "fpo"

    def abrirConexion(self):
        import mysql.connector

        mydb = mysql.connector.connect(
            host=self.servidor,
            user=self.usuario,
            password=self.clave,
            database=self.basedatos
        )
        return mydb