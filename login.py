from tkinter import *
from tela_principal import Aplication
from PIL import Image, ImageTk

# Caminho para o arquivo de usuários
CAMINHO_ARQUIVO = "usuarios.txt"

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Verum Carbo")
        self.root.geometry("600x400")
        self.root.configure(background='#1e3743')
        self.root.resizable(False, False)

        # Carregar a imagem
        self.image = Image.open("LOGO-VERUM-CARBO-Black-400-pixels.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # Label para exibir a imagem na parte superior
        self.label_image = Label(self.root, image=self.photo, bg='#1e3743')
        self.label_image.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.3)

        # Elementos de login
        self.label_usuario = Label(self.root, text="Email", bg='#1e3743', fg='white', font=('Arial', 14))
        self.label_usuario.place(relx=0.13, rely=0.41)

        self.label_senha = Label(self.root, text="Senha", bg='#1e3743', fg='white', font=('Arial', 14))
        self.label_senha.place(relx=0.13, rely=0.51)

        self.entry_usuario = Entry(self.root, font=('Arial', 14))
        self.entry_usuario.place(relx=0.29, rely=0.43, relwidth=0.5)

        self.entry_senha = Entry(self.root, show='*', font=('Arial', 14))
        self.entry_senha.place(relx=0.29, rely=0.53, relwidth=0.5)

        self.btn_login = Button(self.root, text="Login", command=self.verificar_login, font=('Arial', 12))
        self.btn_login.place(relx=0.3, rely=0.7, relwidth=0.4)

        self.btn_cadastro = Button(self.root, text="Cadastrar", command=self.abrir_tela_cadastro, font=('Arial', 12))
        self.btn_cadastro.place(relx=0.3, rely=0.8, relwidth=0.4)

    def verificar_login(self):
        email = self.entry_usuario.get()
        senha = self.entry_senha.get()

        nome_usuario = self.verificar_usuario_em_arquivo(email, senha)
        if nome_usuario:
            self.abrir_tela_principal(nome_usuario)
        else:
            self.label_erro = Label(self.root, text="Login ou senha incorretos", bg='#1e3743', fg='red', font=('Arial', 12))
            self.label_erro.place(relx=0.3, rely=0.6)

    def verificar_usuario_em_arquivo(self, email, senha):
        try:
            with open(CAMINHO_ARQUIVO, "r") as file:
                for linha in file:
                    dados = linha.strip().split(',')
                    if len(dados) >= 4:
                        email_arquivo, senha_arquivo, id_usuario_arquivo, nome_usuario_arquivo = dados
                        if email_arquivo == email and senha_arquivo == senha:
                            return nome_usuario_arquivo
            return None
        except FileNotFoundError:
            return None

    def abrir_tela_principal(self, nome_usuario):
        # Fechar janela de login
        self.root.destroy()

        # Abrir a tela principal
        root_principal = Tk()
        app = Aplication(root_principal, nome_usuario)

    def abrir_tela_cadastro(self):
        # Criar nova janela para cadastro
        self.cadastro_window = Toplevel(self.root)
        self.cadastro_window.title("Cadastro")
        self.cadastro_window.geometry("600x400")
        self.cadastro_window.configure(background='#1e3743')
        self.cadastro_window.resizable(False, False)

        label_nome_usuario = Label(self.cadastro_window, text="Nome Usuário", bg='#1e3743', fg='white', font=('Arial', 14))
        label_nome_usuario.place(relx=0.12, rely=0.1)

        label_novo_usuario = Label(self.cadastro_window, text="Novo Email", bg='#1e3743', fg='white', font=('Arial', 14))
        label_novo_usuario.place(relx=0.12, rely=0.2)

        label_nova_senha = Label(self.cadastro_window, text="Nova Senha", bg='#1e3743', fg='white', font=('Arial', 14))
        label_nova_senha.place(relx=0.12, rely=0.3)

        self.entry_nome_usuario = Entry(self.cadastro_window, font=('Arial', 14))
        self.entry_nome_usuario.place(relx=0.34, rely=0.1, relwidth=0.5)

        self.entry_novo_usuario = Entry(self.cadastro_window, font=('Arial', 14))
        self.entry_novo_usuario.place(relx=0.34, rely=0.2, relwidth=0.5)

        self.entry_nova_senha = Entry(self.cadastro_window, show='*', font=('Arial', 14))
        self.entry_nova_senha.place(relx=0.34, rely=0.3, relwidth=0.5)

        # Radiobuttons para selecionar entre Pessoa Física e Jurídica
        self.tipo_usuario = StringVar(value="Fisica")

        rb_fisica = Radiobutton(self.cadastro_window, text="Pessoa Física", variable=self.tipo_usuario, value="Fisica", bg='#1e3743', fg='white', font=('Arial', 12), command=self.mostrar_campo_id)
        rb_fisica.place(relx=0.15, rely=0.4)

        rb_juridica = Radiobutton(self.cadastro_window, text="Pessoa Jurídica", variable=self.tipo_usuario, value="Juridica", bg='#1e3743', fg='white', font=('Arial', 12), command=self.mostrar_campo_id)
        rb_juridica.place(relx=0.45, rely=0.4)

        # Inicialmente exibe o campo de CPF
        self.label_id = Label(self.cadastro_window, text="CPF", bg='#1e3743', fg='white', font=('Arial', 14))
        self.label_id.place(relx=0.2, rely=0.5)

        self.entry_id = Entry(self.cadastro_window, font=('Arial', 14))
        self.entry_id.place(relx=0.3, rely=0.5, relwidth=0.5)

        btn_salvar = Button(self.cadastro_window, text="Salvar", command=self.salvar_usuario, font=('Arial', 14))
        btn_salvar.place(relx=0.3, rely=0.7, relwidth=0.4)

        # Label de status
        self.label_status = Label(self.cadastro_window, bg='#1e3743', fg='green', font=('Arial', 12))
        self.label_status.place(relx=0.3, rely=0.8)

    def mostrar_campo_id(self):
        # Alterna entre CPF e CNPJ com base na seleção
        if self.tipo_usuario.get() == "Fisica":
            self.label_id.config(text="CPF")
        else:
            self.label_id.config(text="CNPJ")

    def verificar_unicidade_campos(self, usuario, nome, id_usuario):
        try:
            with open(CAMINHO_ARQUIVO, "r") as file:
                for linha in file:
                    dados = linha.strip().split(',')
                    if len(dados) >= 4:
                        usuario_arquivo, senha_arquivo, id_usuario_arquivo, nome_usuario_arquivo = dados
                        if (usuario_arquivo == usuario or 
                            nome_usuario_arquivo == nome or 
                            id_usuario_arquivo == id_usuario):
                            return False
            return True
        except FileNotFoundError:
            # Arquivo não encontrado, todos os campos são únicos por padrão
            return True

    def salvar_usuario_em_arquivo(self, usuario, senha, id_usuario, nome_usuario):
        with open(CAMINHO_ARQUIVO, "a") as file:
            file.write(f"{usuario},{senha},{id_usuario},{nome_usuario}\n")

    def salvar_usuario(self):
        email_usuario = self.entry_novo_usuario.get()
        nova_senha = self.entry_nova_senha.get()
        id_usuario = self.entry_id.get()
        nome_usuario = self.entry_nome_usuario.get()

        if email_usuario and nova_senha and id_usuario and nome_usuario:
            if not self.verificar_unicidade_campos(email_usuario, nome_usuario, id_usuario):
                self.label_status.config(text="Dados já existentes no sistema!", fg='red')
            else:
                # Salvar usuário em arquivo
                self.salvar_usuario_em_arquivo(email_usuario, nova_senha, id_usuario, nome_usuario)
                self.label_status.config(text="Usuário cadastrado com sucesso!", fg='green')
        else:
            self.label_status.config(text="Preencha todos os campos!", fg='red')

# Executando a aplicação de login
if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
