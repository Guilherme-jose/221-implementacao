import tkinter as tk
import os
import shutil
from tkinter import Toplevel, ttk, filedialog
import json
from activity import activity
from consumo import consumo


class tab:
    def __init__(self, root, type = '', account = None):
        self.root = root
        self.type = type
        self.account = account
        self.acts = []
        self.file = []
        
    def show(self):
        pass
    
    def open_event_screen(self):

        def upload_file():
            arquivos_selecionados = filedialog.askopenfilenames(title="Selecione os arquivos")

            # Cria a pasta 'anexos' caso não exista
            anexos = os.path.join(os.getcwd(), 'anexos')
            if not os.path.exists(anexos):
                os.makedirs(anexos)

            # Copia os arquivos para a pasta 'anexos'
            for arquivo in arquivos_selecionados:
                nome_arquivo = os.path.basename(arquivo)
                destino = os.path.join(anexos, nome_arquivo)
                shutil.copy2(arquivo, destino)  # Copia o arquivo 
                self.file.append(nome_arquivo)

        if self.type == 'energy':
            popup_window = Toplevel(self.root)
            consumos_label = ttk.Label(popup_window, text='Consumo:')
            consumos_label.pack()
            consumos_text_box_title = ttk.Entry(popup_window)
            consumos_text_box_title.pack()
            
            periodo_label = ttk.Label(popup_window, text='Período:')
            periodo_label.pack()
            periodo_entry = ttk.Entry(popup_window)
            periodo_entry.pack()
        
        else:
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
            
            upload_button = ttk.Button(popup_window, text='Adicionar anexo', command=upload_file)
            upload_button.pack(side=tk.RIGHT)
            
        def submit():
            
            if self.type == 'energy':
                consumos = consumos_text_box_title.get()
                periodo = periodo_entry.get()

            else:
                titulo = titulo_text_box_title.get()
                valor = valor_entry.get()
                responsavel = responsavel_entry.get()
                beneficiario = beneficiario_entry.get()
                local = local_entry.get()
                data = data_entry.get()
            
            if self.type == 'energy':
                file = ';'.join(self.file)
                self.file = []
                act = consumo(consumos, periodo, 'energy', file)
                act.register()
                del act
            else:
                file = ';'.join(self.file)
                self.file = []
                act = activity(titulo, valor, responsavel, beneficiario, local, data, self.type, '', file, self.account.get_username())
                act.register()
                del act

            
            popup_window.destroy()
            self.display_activities(self.type)
            
        button = ttk.Button(popup_window, text='Submit', command=submit)
        button.pack(side=tk.RIGHT)

    def display_activities(self, type):
        for i in self.acts:
            i.pack_forget()
        
        if self.type == 'energy':
            with open('activities.json', 'r') as f:
                activities = json.loads(f.read())
                
            for act in activities:
                if act['type'] == type:
                    act_label = ttk.Label(self.root, text=act['consumos'] + ' ' + act['periodo'])
                    act_label.pack()
                    self.acts.append(act_label)
        else:
            activities = []
            with open('activities.json', 'r') as f:
                activities = json.loads(f.read())
            
            for act in activities:
                if act['type'] == type:
                    act_label = ttk.Label(self.root, text=act['name'] + ' ' + act['value'] + ' ' + act['asignee'] + ' ' + act['beneficiary'] + ' ' + act['local'] + ' ' + act['date'])
                    act_label.pack()
                    self.acts.append(act_label)
