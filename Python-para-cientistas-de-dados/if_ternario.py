"""
Permite escrever uma condição em uma única linha.
Composto por 3 partes:
    retorno caso verdadeiro
    expressão lógica
    retorno caso expressão não atendida
    """

saldo = 1000
saque = 5000

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")