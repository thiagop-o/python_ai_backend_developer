from datetime import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = datetime.now().year
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Thiago", 1986)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")