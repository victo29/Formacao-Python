class Conta:
    def __init__(self, nro_agencia):
        self._saldo = 0
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001")

conta.depositar(100)
conta.depositar(100)
conta.depositar(100)
conta.depositar(100)
conta.sacar(110)
print(conta.mostrar_saldo())