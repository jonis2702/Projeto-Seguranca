import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from gerar_chaves import gerar_chaves_rsa, gerar_chave_aes
from assinar_arquivo import assinar_arquivo
from cifrar_arquivo import cifrar_arquivo
from verificar_assinatura import verificar_assinatura
from descriptografar_arquivo import descriptografar_arquivo
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Criptografia")
        self.root.geometry("600x450")
        
        # Variáveis para controle
        self.arquivo = None
        self.chave_privada = None
        self.chave_publica = None
        self.chave_aes = None
        self.log_text = ""

        # Layout principal
        self.setup_ui()

    def setup_ui(self):
        """Configura a interface gráfica."""
        # Botões principais
        tk.Button(self.root, text="1. Gerar Chaves", command=self.gerar_chaves).pack(pady=10)
        tk.Button(self.root, text="2. Selecionar Arquivo", command=self.selecionar_arquivo).pack(pady=10)
        tk.Button(self.root, text="3. Assinar Arquivo", command=self.assinar).pack(pady=10)
        tk.Button(self.root, text="4. Cifrar Arquivo", command=self.cifrar).pack(pady=10)
        tk.Button(self.root, text="5. Descriptografar Arquivo", command=self.descriptografar).pack(pady=10)
        tk.Button(self.root, text="6. Verificar Assinatura", command=self.verificar).pack(pady=10)

        # Botão para reiniciar o processo
        tk.Button(self.root, text="Reiniciar Processo", command=self.reiniciar_processo, bg="red", fg="white").pack(pady=10)

        # Indicador de progresso
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        
        # Log de operações
        self.log_label = tk.Label(self.root, text="Logs:", anchor="w")
        self.log_label.pack(fill="x")
        self.log_box = tk.Text(self.root, height=10, state="disabled")
        self.log_box.pack(fill="both", expand=True)

    def atualizar_log(self, mensagem):
        """Atualiza o log com uma nova mensagem."""
        self.log_text += f"{mensagem}\n"
        self.log_box.configure(state="normal")
        self.log_box.delete(1.0, "end")
        self.log_box.insert("end", self.log_text)
        self.log_box.configure(state="disabled")
    
    def reiniciar_processo(self):
        """Reinicia o processo e limpa os dados."""
        self.arquivo = None
        self.chave_privada = None
        self.chave_publica = None
        self.chave_aes = None
        self.log_text = ""
        self.atualizar_log("Processo reiniciado!")
        self.progress["value"] = 0

    def gerar_chaves(self):
        """Gera as chaves RSA e AES."""
        try:
            self.chave_privada, self.chave_publica = gerar_chaves_rsa()
            self.chave_aes = gerar_chave_aes()
            self.atualizar_log("Chaves RSA e AES geradas com sucesso!")
            self.progress["value"] = 20
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar chaves: {e}")

    def selecionar_arquivo(self):
        """Seleciona um arquivo para processar."""
        self.arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
        if self.arquivo:
            self.atualizar_log(f"Arquivo selecionado: {self.arquivo}")
            self.progress["value"] = 40
        else:
            messagebox.showwarning("Atenção", "Nenhum arquivo foi selecionado.")

    def assinar(self):
        """Assina o arquivo selecionado."""
        if not self.arquivo or not self.chave_privada:
            messagebox.showwarning("Atenção", "Gere as chaves e selecione um arquivo antes de continuar.")
            return
        try:
            assinar_arquivo(self.arquivo, self.chave_privada)
            self.atualizar_log("Arquivo assinado com sucesso!")
            self.progress["value"] = 60
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao assinar arquivo: {e}")

    def cifrar(self):
        """Cifra o arquivo selecionado."""
        if not self.arquivo or not self.chave_aes:
            messagebox.showwarning("Atenção", "Gere as chaves e selecione um arquivo antes de continuar.")
            return
        try:
            cifrar_arquivo(self.arquivo, self.chave_aes)
            self.atualizar_log("Arquivo cifrado com sucesso!")
            self.progress["value"] = 80
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cifrar arquivo: {e}")

    def descriptografar(self):
        """Descriptografa o arquivo cifrado."""
        try:
            descriptografar_arquivo("arquivo_cifrado.bin", self.chave_aes)
            self.atualizar_log("Arquivo descriptografado com sucesso!")
            self.progress["value"] = 100
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao descriptografar arquivo: {e}")

    def verificar(self):
        """Verifica a assinatura do arquivo."""
        try:
            verificar_assinatura(self.arquivo, "assinatura.bin", self.chave_publica)
            self.atualizar_log("Assinatura verificada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao verificar assinatura: {e}")

# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
