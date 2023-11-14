from flask import request
from flask_restful import  Resource
import json

lista_habilidades = ['Python','Java','Flask','Ruby','C++']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = request.data
        lista_habilidades.append(json.loads(dados))
        return lista_habilidades

class AlteraHabilidades(Resource):

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluído'}

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return lista_habilidades

