#HERANÇA
class Passaro:
    def voar(self):
        print("Voando .... ^^ ")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avetruz não voa")

#POLIMORFISMO: 
#UMA FUNÇÃO RECEBE UM ATRIBUTO QUALQUER E CHAMA UM MÉTODO
def plano_de_voo(objeto):
    objeto.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)