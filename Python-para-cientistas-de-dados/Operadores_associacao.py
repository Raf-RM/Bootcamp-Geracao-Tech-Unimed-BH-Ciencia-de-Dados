"""Verifica se um objeto está presente alguma sequẽncia (strings, listas,..)
"""
curso = "curso de python"
frutas = ["laranja", "uva", "limão"]
saques = [1000, 200]

resposta_1 = "python" in curso
print(resposta_1)

resposta_2 = "laranja" in frutas
print(resposta_2)

resposta_3 = "banana" in frutas
print(resposta_3)

resposta_4 = 500 in saques
print(resposta_4)

resposta_5 = 200 in saques
print(resposta_5)