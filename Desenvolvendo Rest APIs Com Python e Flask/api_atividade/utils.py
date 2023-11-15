from models import Pessoas
def insere_pessoa():
    pessoa = Pessoas(nome="Rodrigo", idade=25)
    print(pessoa)
    pessoa.save()
def consultar_todos():
    pessoa = Pessoas.query.all()
    print(pessoa)

def consulta_unica(name):
    pessoa = Pessoas.query.filter_by(nome=name).first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Victor').first()
    pessoa.idade = 100
    pessoa.save()

def exclui_pessoa(name):
    pessoa = Pessoas.query.filter_by(nome= name ).first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoa()
    exclui_pessoa("Rodrigo")
    consultar_todos()
    #altera_pessoa()
    #consulta_unica("Victor")