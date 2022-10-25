"""
O operador de identidade é definido pelo is e verifica se ambos ocupam mesmo espaço de memoria.
No exemplo abaixo verifica se curso e nome_curso apontam para o mesmo objeto
assim como se saldo e limite apontam para o mesmo objeto.
"""

curso = "curso de python"
nome_curso = curso
saldo, limite = 200, 200

resposta_1 = curso is nome_curso
print(resposta_1)

resposta_2 = saldo is limite
print(resposta_2)
