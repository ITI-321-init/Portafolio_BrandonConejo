from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017/')
db = client['artesanias']
artistas_collection = db['artistas']
obras_collection = db['obras']


@app.route('/artistas', methods=['POST'])
def registrar_artista():
    datos = request.json
    resultado = artistas_collection.insert_one(datos)
    return jsonify({"message": "Artista registrado", "id": str(resultado.inserted_id)}), 201


@app.route('/artistas/<id>', methods=['PUT'])
def modificar_artista(id):
    datos = request.json
    resultado = artistas_collection.update_one({"_id": id}, {"$set": datos})
    if resultado.matched_count == 0:
        return jsonify({"message": "Artista no encontrado"}), 404
    return jsonify({"message": "Artista modificado"})


@app.route('/artistas/<id>', methods=['DELETE'])
def eliminar_artista(id):
    obras_collection.delete_many({"id_artista": id})
    resultado = artistas_collection.delete_one({"_id": id})
    if resultado.deleted_count == 0:
        return jsonify({"message": "Artista no encontrado"}), 404
    return jsonify({"message": "Artista y sus obras eliminados"})


@app.route('/obras', methods=['POST'])
def registrar_obra():
    datos = request.json
    resultado = obras_collection.insert_one(datos)
    return jsonify({"message": "Obra registrada", "id": str(resultado.inserted_id)}), 201


@app.route('/obras/<id>', methods=['PUT'])
def modificar_obra(id):
    datos = request.json
    resultado = obras_collection.update_one({"_id": id}, {"$set": datos})
    if resultado.matched_count == 0:
        return jsonify({"message": "Obra no encontrada"}), 404
    return jsonify({"message": "Obra modificada"})


@app.route('/obras/<id>', methods=['DELETE'])
def eliminar_obra(id):
    resultado = obras_collection.delete_one({"_id": id})
    if resultado.deleted_count == 0:
        return jsonify({"message": "Obra no encontrada"}), 404
    return jsonify({"message": "Obra eliminada"})


@app.route('/obras/artist/<id_artista>', methods=['GET'])
def consultar_obras_artista(id_artista):
    obras = list(obras_collection.find({"id_artista": id_artista}))
    return jsonify(obras)


@app.route('/obras/categoria/<categoria>', methods=['GET'])
def consultar_obras_categoria(categoria):
    obras = list(obras_collection.find({"categoria": categoria}, {"_id": 1, "nombre": 1, "url_imagen": 1}))
    return jsonify(obras)


@app.route('/obras/<id>', methods=['GET'])
def consultar_detalles_obra(id):
    obra = obras_collection.find_one({"_id": id})
    if not obra:
        return jsonify({"message": "Obra no encontrada"}), 404
    artista = artistas_collection.find_one({"_id": obra['id_artista']})
    return jsonify({"obra": obra, "artista": artista})

if __name__ == '__main__':
    app.run(debug=True)
