from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Função para gerar o hash de um arquivo
def gerar_hash_arquivo(arquivo):
    hash_obj = SHA256.new()
    with open(arquivo, "rb") as file:
        while chunk := file.read(4096):
            hash_obj.update(chunk)
    return hash_obj

# Função para assinar um arquivo com a chave privada RSA
def assinar_arquivo(arquivo, chave_privada):
    hash_arquivo = gerar_hash_arquivo(arquivo)

    # Assinando com a chave privada
    signature = pkcs1_15.new(chave_privada).sign(hash_arquivo)

    # Salvando a assinatura em um arquivo
    with open("assinatura.bin", "wb") as signature_file:
        signature_file.write(signature)
    
    print(f"Arquivo '{arquivo}' assinado com sucesso!")
    return signature
