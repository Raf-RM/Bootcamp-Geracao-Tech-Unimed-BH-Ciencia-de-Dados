class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado  = acordado
    
    def latir(self):
        print("Auau!")

    def dormir(self):
        self.acordado = False
        print("ZzzZzZzzZZz...")

dog_1 = Cachorro("Poly", "creme")
dog_2 = Cachorro("Bingo","marrom", False)

dog_1.latir()
print(dog_1.acordado)

dog_2.dormir()

dog_1.dormir()
print(dog_1.acordado)
