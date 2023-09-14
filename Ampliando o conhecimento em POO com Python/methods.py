class Pessoa: 
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade): #Nâo precisa do contexto de classe nem de objeto
        return idade >= 18
    

p1 = Pessoa.criar_de_data_nascimento(2008,2,13,'Rolildo')

print(p1.nome,p1.idade)

print(Pessoa.e_maior_idade(18))