class Conta:
    def __init__(self, numero_agencia, saldo = 0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
#O ATRIBUTO _saldo SERIA ENTÃO, POR CONVENSÃO, DO TIPO PRIVADO 
#UMA VEZ QUE COMEÇA COM UNDERLINE "_" ENQUANTO O NÚMERO DA 
#AGENCIA SERIA PÚBLICO.


#AMBOS OS MÉTODOS depositar E sacar SÃO PÚBLICOS
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)

print(f"Agência: {conta.numero_agencia}")
conta.depositar(25)
print(f"Após o deposito o valor em conta é de: {conta.mostrar_saldo()}")
conta.sacar(50)
print(f"Após o saque o valor em conta é de: {conta.mostrar_saldo()}")
