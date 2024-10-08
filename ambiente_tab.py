from tkinter import Toplevel, ttk
import tkinter as tk
from tab import tab

class ambiente_tab(tab):
    def __init__(self, root, type='ambiente', account=None):
        super().__init__(root, type, account)
        
    def show(self):
        ttk.Label(self.root, text='Feitos Ambientais').pack()
        # Create a button to open the event screen
        open_event_button = ttk.Button(self.root, text='Adicionar Consumo', command=self.open_event_screen)
        open_event_button.pack()
        
        self.display_activities('ambiente')