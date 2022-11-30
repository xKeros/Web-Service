from psycopg2 import connect, extras

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