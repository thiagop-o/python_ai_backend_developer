class Veiculo:
    def __init__(self, cor, placa, quantidade_rodas):
        self.cor = cor
        self.placa = placa
        self.quantidade_rodas = quantidade_rodas

    def ligar_motor(self):
        print("Ligando Motor")
        
    def __str__(self):
        return f"{self.__class__.__name__} foi criada com sucesso, com os parametros {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
        

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, quantidade_rodas, carregado: bool):
        super().__init__(cor, placa, quantidade_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Nao'}')


moto = Motocicleta("Preta", "abc-1234", 2)
print(moto)

caminhao = Caminhao("roxo", "cba-9537", 8, True)
caminhao.esta_carregado()