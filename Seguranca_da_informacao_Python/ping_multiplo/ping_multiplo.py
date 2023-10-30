import os
import time

# Acessando o arquivo host.txt
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines() # Formatando o texto

    # iterando a variavel que contem os dados do arquivo
    for ip in dump:
        print('Verificando o ip', ip)
        # chamando o método os.system e passando o ip
        os.system('ping -n 2 {}'.format(ip))
        print("-" * 60)
        # Adicionando um tempo de espera
        time.sleep(5)
