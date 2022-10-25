""" 
Programa on seja informada cor, modelo ano 
e valor da bicicleta e que tenha os compotamentos
buzinar, parar e correr.
"""
class Bicicleta:
 #INICIALIZANDO AS CARACTERISTICAS DA CLASSE (ATRIBUTOS)
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

 #MÉTODOS DA CLASSE   
    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vrunnnnn...")

    def buzinar(self):
        print("trin trin!!")

    # 
    #def __str__(self):
    #    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"   

bike_1 = Bicicleta("vermelho e azul","Soul Chamonix",2022,8000.00)
print(bike_1.cor)
print(bike_1.modelo)
print(bike_1.ano)
print(bike_1.valor)

bike_1.buzinar()
bike_1.correr()
bike_1.parar()

bike_2 = Bicicleta("Preto","First Athmos",2018,3000.0)
Bicicleta.buzinar(bike_2) # é igual a bike_2.buzinar(), com def buzinar(self)

print(bike_2)
print(bike_1)