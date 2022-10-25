class Pessoa:
    def __init__(self,nome=None, idade=None):
        self. nome = nome
        self.idade = idade
    
#APLICANDO O DECORADOR @classMethod TRANSFORMAMOS O METODO 
#EM UM METODO DE CLASSE. cls É A REFERENCIA PARA A CLASSE
#OU SEJA, APONTA PARA A CLASSE Pessoa
    @classmethod
    def criar_por_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

#APLICANDO O DECORADOR @staticmethod TRASFORMAMOS A FUNÇÃO
#EM UM MÉTODO ESTÁTICO
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
        
pessoa_1 = Pessoa("Rafa", 31)
print(pessoa_1.nome, pessoa_1.idade)

pessoa_2 = Pessoa.criar_por_data_nascimento(1991, 3, 11, "Rafael")
print(pessoa_2.nome, pessoa_2.idade)

print(Pessoa.maior_idade(14))
print(Pessoa.maior_idade(20))