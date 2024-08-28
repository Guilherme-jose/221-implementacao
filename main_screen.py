import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from screen import screen
from main_tab import main_tab
from social_tab import social_tab
from ambiente_tab import ambiente_tab
from governanca_tab import governanca_tab
from energy_tab import energy_tab
from PIL import Image, ImageTk

class main_screen(screen):
    def __init__(self, root):
        self.root = root
        self.nome_usuario = 'Usuário'
        self.tela()
        self.frames_da_tela()
        self.root.mainloop()

    def tela(self):
        self.root.title("Verum Cabo")
        self.root.configure(background='#1e3743')
        self.root.geometry("1100x900")
        self.root.resizable(False, False)

    def frames_da_tela(self):
        self.image_verum_carbo = Image.open("logo.png")
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
        self.tab_control = ttk.Notebook(self.frame_1)
        tabs = ['MAIN', 'AMBIENTE', 'SOCIAL', 'GOVERNANÇA', 'RELATÓRIOS', 'ENERGIA']
        tabs_ref = []
        
        for i in range(1, 7):
            tab = tk.Frame(self.tab_control)
            self.tab_control.add(tab, text=tabs[i-1])
            tabs_ref.append(tab)

        mt = main_tab(tabs_ref[0])
        mt.show()

        st = ambiente_tab(tabs_ref[1])
        st.show()
        
        st = social_tab(tabs_ref[2])
        st.show()

        st = governanca_tab(tabs_ref[3])
        st.show()

        st = energy_tab(tabs_ref[5])
        st.show()
        
        # Colocar o Notebook dentro do frame_1
        self.tab_control.place(relwidth=1, relheight=1)

        # Adicionar botões para escrever relatórios em cada aba
        self.add_report_buttons()

    def add_report_buttons(self):
        tabs = [self.tab_main, self.tab_ambiente, self.tab_social, self.tab_governanca, self.tab_relatorios]
        tab_names = ["Main", "Ambiente", "Social", "Governança", "Relatórios"]
        
        for i, tab in enumerate(tabs):
            btn = Button(tab, text=f"Escrever Relatório {tab_names[i]}", command=lambda t=tab_names[i]: self.open_report_form(t))
            btn.pack(pady=10)

    def open_report_form(self, tab_name):
        form_window = Toplevel(self.root)
        form_window.title(f"Relatório - {tab_name}")

        labels = ["Título", "Beneficiário", "Responsável", "Valor", "Local", "Data", "Descrição"]
        entries = {}

        for i, label_text in enumerate(labels):
            Label(form_window, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky=W)
            entry = Entry(form_window, width=50)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[label_text] = entry

        def save_report():
            report_data = {label: entry.get() for label, entry in entries.items()}
            report_text = "\n".join([f"{key}: {value}" for key, value in report_data.items()])
            
            file_path = f"{tab_name}_report.txt"
            with open(file_path, "a") as file:
                file.write(f"\n--- Novo Relatório ---\n{report_text}\n")
            
            self.display_report(tab_name)
            form_window.destroy()

        Button(form_window, text="Salvar Relatório", command=save_report).grid(row=len(labels), column=1, pady=10)

    def display_report(self, tab_name):
        file_path = f"{tab_name}_report.txt"
        if not os.path.exists(file_path):
            return
        
        with open(file_path, "r") as file:
            report_text = file.read()

        tab = self.notebook.nametowidget(self.notebook.select())
        for widget in tab.winfo_children():
            widget.destroy()
        
        text_widget = Text(tab, wrap=WORD)
        text_widget.insert(INSERT, report_text)
        text_widget.pack(expand=1, fill=BOTH)