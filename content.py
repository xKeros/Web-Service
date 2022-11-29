from flask import request, jsonify
from psycopg2 import connect, extras

#parametros de la base de datos
host = 'localhost'
port = 5432
dbname = 'db_circuito03'
user = 'postgres'
password = '1234'

#Connection with database ------ Conexion con base de datos 
def get_database():
    conn = connect(host=host, port=port, dbname=dbname,
                   user=user, password=password)
    return conn
#generate key for encryption----- Generacion de encriptacion



#Into data in database -------- Ingresar datos en la base de datos
def into_content():
    new_content = request.get_json()
    content = new_content['contenido']
    header = new_content['encabezado']

    print(content, header )

    conn = get_database()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("INSERT INTO tb_contenido(contenido, encabezado) VALUES (%s, %s) RETURNING *",
                (content, header))
    result = cur.fetchone()

    print(result)

    conn.commit()

    cur.close()
    conn.close()

    return jsonify(result)

#Get the contents of database ------- Obtener el contenidos de la base de datos
def obtener_content():
    conn = get_database()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM tb_contenido")
    result1 = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(result1)
#Get the content of database ------- Obtener el contenido de la base de datos

def obtener_contenido(id):
    conn = get_database()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("SELECT * FROM tb_contenido WHERE id_contenido =%s", (id,))
    content = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(content)


#DELETE content from database ------ Eliminar contenido de la base de datos
def eliminar_contenido(id):
    conn = get_database()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute("DELETE FROM tb_contenido WHERE id_contenido =%s  RETURNING *", (id,))
    result1 = cur.fetchall()

    if result1 is None:
        return jsonify({"message": "User not found"}), 404

    print(result1)

    conn.commit()
    cur.close()
    conn.close()

    return jsonify(result1)

#Update content of content ------- Actualizar el contenido
def actualizar_contenido(id):

    new_content = request.get_json()
    content = new_content['contenido']
    header = new_content['encabezado']


    conn = get_database()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)


    cur.execute("UPDATE tb_contenido SET contenido = %s, encabezado = %s WHERE id_contenido = %s RETURNING *",(content, header, id))
    result = cur.fetchall()


    conn.commit()

    cur.close()
    conn.close()

    return jsonify(result)