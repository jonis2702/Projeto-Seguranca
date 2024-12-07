from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Função para cifrar um arquivo usando a chave AES
def cifrar_arquivo(arquivo, chave_aes):
    with open(arquivo, "rb") as file:
        dados = file.read()

    cipher = AES.new(chave_aes, AES.MODE_CBC)
    dados_cifrados = cipher.encrypt(pad(dados, AES.block_size))

    with open("arquivo_cifrado.bin", "wb") as enc_file:
        enc_file.write(cipher.iv)  # Salvando o IV
        enc_file.write(dados_cifrados)  # Salvando os dados cifrados
    
    print(f"Arquivo '{arquivo}' cifrado com sucesso!")
    return cipher.iv, dados_cifrados
