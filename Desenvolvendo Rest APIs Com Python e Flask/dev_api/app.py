from flask import Flask, jsonify, request
import json
app = Flask(__name__)

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

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagemErro = f'Desenvolvedor de ID {id} não existe'
            response = {'status':'erro', 'mensagem': mensagemErro }
        except Exception:
            mensagemErro = f'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagemErro}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return  jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluído'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    else:
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)