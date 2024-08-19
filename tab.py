import tkinter as tk
from tkinter import Toplevel, ttk

from activity import activity


class tab:
    def __init__(self, root, type = ''):
        self.root = root
        self.type = type
        self.acts = []
        
    def show(self):
        pass
    
    def open_event_screen(self):

        popup_window = Toplevel(self.root)
        titulo_label = ttk.Label(popup_window, text='Título:')
        titulo_label.pack()
        titulo_text_box_title = ttk.Entry(popup_window)
        titulo_text_box_title.pack()
        
        valor_label = ttk.Label(popup_window, text='Valor:')
        valor_label.pack()
        valor_entry = ttk.Entry(popup_window)
        valor_entry.pack()
        
        responsavel_label = ttk.Label(popup_window, text='Responsável:')
        responsavel_label.pack()
        responsavel_entry = ttk.Entry(popup_window)
        responsavel_entry.pack()
        
        beneficiario_label = ttk.Label(popup_window, text='Beneficiário:')
        beneficiario_label.pack()
        beneficiario_entry = ttk.Entry(popup_window)
        beneficiario_entry.pack()

        local_label = ttk.Label(popup_window, text='Local:')
        local_label.pack()
        local_entry = ttk.Entry(popup_window)
        local_entry.pack()
        
        data_label = ttk.Label(popup_window, text='Data:')
        data_label.pack()
        data_entry = ttk.Entry(popup_window)
        data_entry.pack()
        
        description_label = ttk.Label(popup_window, text='Descrição:')
        description_label.pack()
        description_text_box = tk.Text(popup_window)
        description_text_box.pack()
        
        upload_button = ttk.Button(popup_window, text='Adicionar anexo', command=self.upload_file)
        upload_button.pack(side=tk.RIGHT)
        
        
        def submit():
            titulo = titulo_text_box_title.get()
            valor = valor_entry.get()
            responsavel = responsavel_entry.get()
            beneficiario = beneficiario_entry.get()
            descricao = description_text_box.get('1.0', tk.END)
            local = local_entry.get()
            data = data_entry.get()
            
            act = activity(titulo, valor, responsavel, beneficiario, local, data, self.type, descricao)
            
            act.register()
            del act
                
            popup_window.destroy()
            self.display_activities(self.type)
            
        button = ttk.Button(popup_window, text='Submit', command=submit)
        button.pack(side=tk.RIGHT)

    def display_activities(self, type):
        for i in self.acts:
            i.pack_forget()
            
        f = open('activities.txt', 'r')
        activities = f.readlines()
        f.close()
        for act in activities:
            act = act.split(',')
            if act[0] == type:
                act_label = ttk.Label(self.root, text=act[1] + ' ' + act[2] + ' ' + act[3] + ' ' + act[4] + ' ' + act[5] + ' ' + act[6])
                act_label.pack()
                self.acts.append(act_label)

