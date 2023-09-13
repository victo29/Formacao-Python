class Person:
    def __init__(self, name, birth_year):
        self._name = name
        self._birth_year = birth_year
    
    @property
    def nome(self):
        return self._name
    
    @property 
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._birth_year

pessoa = Person('Wellington Rato', 1999)
print(f"O nome do usuário é {pessoa.nome}, e sua idade é {pessoa.idade}")