from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Função para descriptografar um arquivo cifrado com a chave AES
def descriptografar_arquivo(arquivo_cifrado, chave_aes):
    with open(arquivo_cifrado, "rb") as enc_file:
        iv = enc_file.read(16)  # Lê o IV
        dados_cifrados = enc_file.read()

    cipher = AES.new(chave_aes, AES.MODE_CBC, iv)
    dados_descompactados = unpad(cipher.decrypt(dados_cifrados), AES.block_size)

    with open("arquivo_descompactado.txt", "wb") as file:
        file.write(dados_descompactados)
    
    print(f"Arquivo '{arquivo_cifrado}' descriptografado com sucesso!")
