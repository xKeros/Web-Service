from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.content import Content
# Models
from models.ContentModel import ContentModel

main = Blueprint('content_blueprint', __name__)


@main.route('/')
def get_contents():
    try:
        contenido = ContentModel.get_contents()
        return jsonify(contenido)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_content(id_publicacion):
    try:
        content = ContentModel.get_content(id)
        if content != None:
            return jsonify(content)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_content():
    try:
        encabezado = request.json['encabezado']
        registro = request.json['registro']
        id_publicacion = uuid.uuid4()
        content = Content(str(id_publicacion), encabezado, registro)

        affected_rows = ContentModel.add_content(contentenido1)

        if affected_rows == 1:
            return jsonify(content.id_publicacion)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_content(id_publicacion):
    try:
        encabezado = request.json['encabezado']
        registro = request.json['registro']
        contenido = Content(id_publicacion, encabezado, registro)

        affected_rows = ContentModel.add_content(contentenido1)

        if affected_rows == 1:
            return jsonify(contenido.id_publicacion)
        else:
            return jsonify({'message': "No content updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_content(id_publicacion):
    try:
        content = Content(id_publicacion)

        affected_rows = ContentModel.delete_content(content)

        if affected_rows == 1:
            return jsonify(content.id_publicacion)
        else:
            return jsonify({'message': "No content deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
