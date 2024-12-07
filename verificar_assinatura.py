from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Função para gerar o hash de um arquivo
def gerar_hash_arquivo(arquivo):
    hash_obj = SHA256.new()
    with open(arquivo, "rb") as file:
        while chunk := file.read(4096):
            hash_obj.update(chunk)
    return hash_obj

# Função para verificar a assinatura de um arquivo usando a chave pública RSA
def verificar_assinatura(arquivo, assinatura, chave_publica):
    hash_arquivo = gerar_hash_arquivo(arquivo)
    with open(assinatura, "rb") as signature_file:
        signature = signature_file.read()

    try:
        pkcs1_15.new(chave_publica).verify(hash_arquivo, signature)
        print(f"A assinatura do arquivo '{arquivo}' é válida!")
    except (ValueError, TypeError):
        print(f"A assinatura do arquivo '{arquivo}' não é válida!")
