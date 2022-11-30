from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from flask_cors import CORS

from models.content import into_content, obtener_content, eliminar_contenido, obtener_contenido, actualizar_contenido






app = Flask(__name__)

#CORS(app, resources={"*", {"origins": "http://localhost:3000"}})

#Rutas contenido------------------------------------------------

@app.get('/content')
def get_contents():
    result  = obtener_content()
    return result


@app.get('/content/<id>')
def obtener_conte(id):
    result = obtener_contenido(id)
    return result

@app.post('/content')
def ingresar_content():
    result = into_content()
    return result


@app.put('/content/<id>')
def update_content(id):
    result = actualizar_contenido(id)
    return result

@app.delete('/content/<id>')
def delete_content(id): 
    result = eliminar_contenido(id)
    return result

#Rutas usuarios------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
