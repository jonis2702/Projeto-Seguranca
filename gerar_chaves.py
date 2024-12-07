from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Geração de chave RSA
def gerar_chaves_rsa():
    chave_privada = RSA.generate(2048)
    chave_publica = chave_privada.publickey()

    # Salvando as chaves em arquivos
    with open("private_key.pem", "wb") as private_file:
        private_file.write(chave_privada.export_key())
    with open("public_key.pem", "wb") as public_file:
        public_file.write(chave_publica.export_key())
    
    print("Chaves RSA geradas com sucesso!")
    return chave_privada, chave_publica

# Geração de chave AES
def gerar_chave_aes():
    chave_aes = get_random_bytes(32)
    with open("aes_key.bin", "wb") as aes_file:
        aes_file.write(chave_aes)
    
    print("Chave AES gerada com sucesso!")
    return chave_aes
