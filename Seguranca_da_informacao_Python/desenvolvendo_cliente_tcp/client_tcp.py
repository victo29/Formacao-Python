import socket
import sys # fornece o acesso a algumas variaveis e algumas funções que tem forte interação com o interpretador
def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro {}".format(e))
        sys.exit() # Fecha o programa
    print("Socke criado com sucesso")

    hostAlvo = input("Digite o host ou ip a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectado: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Client tcp conectado com sucesso")
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()