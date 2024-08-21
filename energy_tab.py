from tkinter import Toplevel, ttk
import tkinter as tk
from tab import tab
from consumo import consumo

class energy_tab(tab):
    def __init__(self, root, type='energy'):
        super().__init__(root, type)
        
    def show(self):
        ttk.Label(self.root, text='Consumo de Energia').pack()
        # Create a button to open the event screen
        open_event_button = ttk.Button(self.root, text='Adicionar Consumo', command=self.open_event_screen)
        open_event_button.pack()
        
        self.display_activities('energy')
    
    
    