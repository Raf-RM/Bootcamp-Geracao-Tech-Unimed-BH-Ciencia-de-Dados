class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def partida(self):
        print("Dando partida no veículo")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"       

class Mocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} esta carregado")

moto = Mocicleta("preta", "ade-2309", 2)
moto.partida()

caminhao = Caminhao("Branco", "hpo-2300",4,False)

print(moto)
print(caminhao)