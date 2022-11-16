from database.db import get_connection
from .entities.content import Content


class ContentModel():

    @classmethod
    def get_contents(self):
        try:
            connection = get_connection()
            contents = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_publicacion, encabezado, registro FROM tbl_publicaciones")
                resultset = cursor.fetchall()

                for row in resultset:
                    contenido = Content(row[0], row[1], row[2])
                    contents.append(contenido.to_JSON())

            connection.close()
            return contents
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_content(self, id_publicacion):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_publicacion, encabezado, registro FROM tbl_publicaciones WHERE id_publicacion = %s", (id_publicacion,))
                row = cursor.fetchone()

                content = None
                if row != None:
                    content = Content(row[0], row[1], row[2])
                    content = content.to_JSON()

            connection.close()
            return content
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_content(self, contentenido1):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO tbl_publicaciones (id_publicacion, encabezado, registro) 
                                VALUES (%s, %s, %s)""", (contentenido1.id_publicacion, contentenido1.encabezado, contentenido1.registro))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_content(self, content):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE tbl_publicaciones SET encabezado = %s, registro = %s 
                                WHERE id = %s""", (content.encabezado, content.registro, content.id_publicacion))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_content(self, content):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM tbl_publicaciones WHERE id_publicacion = %s", (content.id_publicacion,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
