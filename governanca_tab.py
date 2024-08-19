from tkinter import Toplevel, ttk
import tkinter as tk
from tab import tab
from governanca import governanca

class governanca_tab(tab):
    def __init__(self, root, type='governança'):
        super().__init__(root, type)
    
    def upload_file(self):
        pass
        
    def show(self):
        ttk.Label(self.root, text='Feitos Governamentais').pack()
        # Create a button to open the event screen
        open_event_button = ttk.Button(self.root, text='Adicionar Feitos', command=self.open_governanca_screen)
        open_event_button.pack()
        
        self.display_activities('governança')