import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Socke criado com sucesso")

host = ('localhost')
porta = 5433

mensagem = "am I connected?"

try:
    #print("Client: " + mensagem)
    s.sendto(mensagem.encode(),(host,5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()

    print("Cliente: " + dados)
finally:
    print("Client: Fechando")
    s.close()