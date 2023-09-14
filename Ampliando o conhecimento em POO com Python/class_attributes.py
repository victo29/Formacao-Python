class Estudante:
    escola = "DIO" #unica para todos os objetos

    def  __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

victor = Estudante("Victor", 1234567)
Iasmin = Estudante("Iasmin", 7654321)

mostrar_valores(victor, Iasmin)