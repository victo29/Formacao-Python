import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = input(""" ###### Escolha o tipo de hash ######
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o número do hash a ser gerado: 
            """)
tipo = ""
if menu == '1':
    resultado = hashlib.md5(string.encode('utf-8'))
    tipo = "MD5"
elif menu == '2':
    resultado = hashlib.sha1(string.encode('utf-8'))
    tipo = "SHA1"
elif menu == '3':
    resultado = hashlib.sha256(string.encode('utf-8'))
    tipo = "SHA256"
elif menu == '4':
    resultado = hashlib.sha512(string.encode('utf-8'))
    tipo = "SHA512"

print(f"O hash {tipo} da string é: ", resultado.hexdigest())