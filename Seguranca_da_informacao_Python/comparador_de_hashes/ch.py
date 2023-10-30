import hashlib
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') #informa o algoritmo que será utilizado

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())


# Digest resume os dados
if hash1.digest() != hash2.digest():
    print("Os arquivos são diferentes")
else:
    print("Os arquivos são iguais")
    print(hash2.hexdigest())
    print(hash1.hexdigest())