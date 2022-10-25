class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"       


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class FalarMixin:
    def falar(self):
        return "Estou falando!"

class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    #def __init__(self, cor_pelo, **kw):
        # ORDEM DE RESOLUÇÃO DOS MÉTODOS
    #    print(Ornitorrinco.__mro__) # ou Ornintorrinco.mro()
    pass


cachorro = Cachorro(numero_patas = 4, cor_pelo = "Amarelo")
print(cachorro)
print()

ornintorrinco = Ornitorrinco(numero_patas = 2, cor_pelo = "Marrom", cor_bico = "Laranja")
print(ornintorrinco)
print(ornintorrinco.falar())

