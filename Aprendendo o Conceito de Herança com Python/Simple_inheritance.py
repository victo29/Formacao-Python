class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Motor ligado")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor,placa,numero_rodas, carregado):
        super().__init__(cor, placa,numero_rodas ) # invoca um método da classe pai
        self.carregado = carregado

    def carregamento(self):
        if self.carregado:
            print("Está com carregamento")
        else: 
            print("Está vazío")
    def buzinar(self):
        print("FOOOOOON... FOOONNN...")

    def __str__(self):
        return self.cor

moto = Motocicleta("preta","abc-1234",2)
print(moto.__dict__) # mostra os atributos do objeto moto (dicionario de objetos)
#moto.ligar_motor()

carro = Carro("branco", "xfe-1456", 4)
#carro.ligar_motor()

caminhao = Caminhao("cinza", "upa-1345", 8, False)
caminhao.ligar_motor()
caminhao.buzinar()
caminhao.carregamento()