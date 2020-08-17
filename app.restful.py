from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Samuel',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Ricardo',
        'habilidades': ['Python', 'Django']}
]

# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Dev de Id'' {} não existe'.format(id)
            response = {'Status': 'Erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administrador do Sistema'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'Sucesso', 'Mensagem': 'Registro excluido'}

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

# lista de desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades,'/habilidades/' )

if __name__ == '__main__':
    app.run(debug=True)
