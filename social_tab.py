from tkinter import Toplevel, ttk
import tkinter as tk
from tab import tab
from activity import activity

class social_tab(tab):
    def __init__(self, root):
        self.root = root
    
    def upload_file(self):
        pass
        
    def show(self):
        ttk.Label(self.root, text='Social Tab').pack()
        # Create a button to open the event screen
        open_event_button = ttk.Button(self.root, text='Open Event Screen', command=self.open_event_screen)
        open_event_button.pack()
    
    
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
        
        upload_button = ttk.Button(popup_window, text='Adicionar anexo', command=self.upload_file)
        upload_button.pack(side=tk.RIGHT)
        
        
        def submit():
            titulo = titulo_text_box_title.get()
            valor = valor_entry.get()
            responsavel = responsavel_entry.get()
            beneficiario = beneficiario_entry.get()
            
            act = activity(titulo, valor, responsavel, beneficiario)
            act.register()
            del act
        
            popup_window.destroy()
            
        button = ttk.Button(popup_window, text='Submit', command=submit)
        button.pack(side=tk.RIGHT)
