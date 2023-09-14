from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando a tv")
    def desligar(self):
        print("desligando a tv")
    
    def marca(self):
        print("LG")


controle = ControleTV()
controle.ligar()
controle.desligar()