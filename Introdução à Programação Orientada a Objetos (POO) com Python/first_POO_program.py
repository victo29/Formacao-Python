class  Bicicleta:
    def __init__(self, cor,modelo,ano,valor): #Método construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.numero_marcha = 1

    
    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando a bicicleta")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummmmmmmmmmmmm...")

    def trocar_marcha(self,nmr_marcha):
        print("Trocando marcha....")

        def _trocar_marcha():
            if nmr_marcha > self.numero_marcha:
                self.numero_marcha = nmr_marcha
                print("Marcha trocada!")
            else: 
                print("Não trocou de marcha")
        _trocar_marcha()
    
    # def __str__(self):
    #     return  f"{self.__class__.__name__}: {self.cor}, {self.modelo}, {self.ano}, {self.valor}" # Retorna todos os atributos
    
    def __str__(self):
        return  f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" # Retorna todos os atributos
    


caloi = Bicicleta("vermelha","caloi", 2022, 600)
caloi.buzinar()
caloi.correr()
caloi.parar()
print(caloi) # Função str

caloi.trocar_marcha(1)

# print(caloi.cor, caloi.modelo)