def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)

sacar(100)
depositar(251)