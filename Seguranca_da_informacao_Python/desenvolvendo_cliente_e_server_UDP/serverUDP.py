import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso")

host = 'localhost'
porta = 5432

s.bind((host, porta))  # faz a ligação do cliente servidor atraves do host e da porta
mensagem = "\nServidor: you are connected"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Server sending message...")
        s.sendto(dados + (mensagem.encode()), end)
