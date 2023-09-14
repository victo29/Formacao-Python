class Passaro:
    def voar(self):
        print("voando....")

class Pardal(Passaro):
    def voar(self):
        return super.voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
