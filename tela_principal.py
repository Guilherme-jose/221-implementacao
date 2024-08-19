from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Aplication:
    def __init__(self, root, nome_usuario):
        self.root = root
        self.nome_usuario = nome_usuario
        self.tela()
        self.frames_da_tela()
        self.root.mainloop()

    def tela(self):
        self.root.title("Verum Cabo")
        self.root.configure(background='#1e3743')
        self.root.geometry("1100x900")
        self.root.resizable(False, False)

    def frames_da_tela(self):
        self.image_verum_carbo = Image.open("LOGO-VERUM-CARBO-Black-400-pixels.png")
        self.foto_verum_carbo = ImageTk.PhotoImage(self.image_verum_carbo)

        self.image_foto_perfil = Image.open("foto_padrao.jpg")
        self.foto_perfil = ImageTk.PhotoImage(self.image_foto_perfil)

        # Frames
        self.frame_1 = Frame(self.root, bd=4, bg="#e0ffff", highlightthickness=3, highlightbackground="#000000")
        self.frame_2 = Frame(self.root, bd=4, bg="#e0ffff", highlightthickness=3, highlightbackground="#000000")
        self.frame_3 = Frame(self.root, bd=4, bg="#006973", highlightthickness=3, highlightbackground="#000000")

        # Label de imagem
        self.label_image = Label(self.frame_3, image=self.foto_verum_carbo)
        self.label_image.place(relwidth=1, relheight=1)

        self.label_image_perfil = Label(self.frame_2, image=self.foto_perfil)
        self.label_image_perfil.place(relx=0.05, rely=0.005, relwidth=0.9, relheight=0.33)

        # Label com o nome do usuário
        self.label_nome_usuario = Label(self.frame_2, text=f"{self.nome_usuario}", bg='#e0ffff', fg='black', font=('Arial', 14))
        self.label_nome_usuario.place(relx=0.36, rely=0.35)

        # Configuração dos Frames
        self.frame_1.place(relx=0.25, rely=0.18, relwidth=0.73, relheight=0.80)
        self.frame_2.place(relx=0.02, rely=0.18, relwidth=0.22, relheight=0.80)
        self.frame_3.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.14)

        # Adicionando o Notebook (abas) ao frame_1
        self.notebook = ttk.Notebook(self.frame_1)
        
        # Criar as abas
        self.tab_main = Frame(self.notebook, bg="#e0ffff")
        self.tab_ambiente = Frame(self.notebook, bg="#e0ffff")
        self.tab_social = Frame(self.notebook, bg="#e0ffff")
        self.tab_governanca = Frame(self.notebook, bg="#e0ffff")
        self.tab_relatorios = Frame(self.notebook, bg="#e0ffff")

        # Adicionar abas ao Notebook
        self.notebook.add(self.tab_main, text="Main")
        self.notebook.add(self.tab_ambiente, text="Ambiente")
        self.notebook.add(self.tab_social, text="Social")
        self.notebook.add(self.tab_governanca, text="Governança")
        self.notebook.add(self.tab_relatorios, text="Relatórios")

        # Colocar o Notebook dentro do frame_1
        self.notebook.place(relwidth=1, relheight=1)
