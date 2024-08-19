from tab import tab
from tkinter import ttk

class main_tab(tab):
    def __init__(self, root):
        self.root = root
        
    def show(self):
        ttk.Label(self.root, text='Main Tab').pack()
