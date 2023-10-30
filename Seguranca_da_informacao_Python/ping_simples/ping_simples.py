import os
# Facilita a utilização de mecanismos do sistema operacional

print('#' * 60)

# recebe o valor do usuário
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")

print('-' * 60)

# Chamando o metodo system  da biblioteca os e passando o comando ping
os.system('ping -n 6 {}'.format(ip_ou_host))

