import pymysql

class DataBase:
    def __init__ (self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='base_peliculas'
        )

        self.cursor = self.connection.cursor()

        print("Conexion establecida exitosamente")

    def select_movie(self, id):
        sql = 'SELECT id_pelicula, titulo, idioma, anio, resumen FROM peliculas WHERE id_pelicula = {}'.format(id)

        try:
            self.cursor.execute(sql)
            movie = self.cursor.fetchone()
            print("Id:", movie[0])
            print("Titulo:", movie[1])
            print("Idioma:", movie[2])
            print("Año:", movie[3])
            print("Resumen:", movie[4])

        except Exception as e:
            raise

    def close(self):
        self.connection.close()
        print("Base de datos cerrada")

database = DataBase()
database.select_movie(2)

database.close()
