from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades
from habilidades import AlteraHabilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
    'id':0,
    'nome':'Victor',
     'habilidades':['Python', 'Flask']
     },
    {
    'id':1,
    'nome':'Iasmin',
     'habilidades':['Figma','Css']
     }
]


class Desenvolvedor(Resource):
    def get(self, id):

        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagemErro = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagemErro}
        except Exception:
            mensagemErro = f'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagemErro}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'registro excluído'}




class listaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')


api.add_resource(listaDesenvolvedores,'/dev/')


api.add_resource(Habilidades, '/habilidades/')

api.add_resource(AlteraHabilidades, '/habilidades/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)
