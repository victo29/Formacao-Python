import time
from  threading import  Thread
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:

        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto {piloto} Km{trajeto}\n')


t_carro1 = Thread(target=carro,args=[1, 'Victor'])
t_carro2 = Thread(target=carro,args=[1.7, 'Samuel'])

t_carro1.start()
t_carro2.start()