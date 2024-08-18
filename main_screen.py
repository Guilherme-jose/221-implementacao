import tkinter as tk
from tkinter import ttk
from screen import screen

class main_screen(screen):
    def __init__(self, root):
        self.root = root
        
    def show(self):
        tab_control = ttk.Notebook(self.root)
        tabs = ['MAIN', 'AMBIENTE', 'SOCIAL', 'GOVERNANÇA', 'RELATÓRIOS']
        
        for i in range(1, 6):
            tab = tk.Frame(tab_control)
            tab_control.add(tab, text=tabs[i-1])
        
        
        tab_control.pack(fill=tk.Y, expand=True)
        side_menu = tk.Frame(self.root, width=200, bg='gray')
        side_menu.pack(side=tk.LEFT, fill=tk.Y)

        # Add menu items to the side menu
        menu_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
        for item in menu_items:
            label = tk.Label(side_menu, text=item, padx=10, pady=5)
            label.pack(anchor=tk.W)