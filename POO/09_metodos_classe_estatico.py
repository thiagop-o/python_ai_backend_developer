from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = datetime.now().year - ano
        return cls(nome, idade) # por convencao chamamos de CLS os metodos de classe

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1986, 12, 11, "Thiago")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(p.idade))
print(Pessoa.e_maior_idade(8))