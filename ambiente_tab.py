from tkinter import Toplevel, ttk
import tkinter as tk
from tab import tab
from gastos import gastos

class ambiente_tab(tab):
    def __init__(self, root, type='ambiente'):
        super().__init__(root, type)
    
    def upload_file(self):
        pass
        
    def show(self):
        ttk.Label(self.root, text='Feitos Ambientais').pack()
        # Create a button to open the event screen
        open_event_button = ttk.Button(self.root, text='Adicionar Consumo', command=self.open_atividade_screen)
        open_event_button.pack()
        
        self.display_activities('ambiente')