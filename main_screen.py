import tkinter as tk
from tkinter import ttk
from screen import screen
from main_tab import main_tab
from social_tab import social_tab
from ambiente_tab import ambiente_tab
from governanca_tab import governanca_tab
from energy_tab import energy_tab

class main_screen(screen):
    def __init__(self, root):
        self.root = root
    
    
    
    def show(self):
        tab_control = ttk.Notebook(self.root)
        tabs = ['MAIN', 'AMBIENTE', 'SOCIAL', 'GOVERNANÇA', 'RELATÓRIOS', 'ENERGIA']
        tabs_ref = []
        
        for i in range(1, 7):
            tab = tk.Frame(tab_control)
            tab_control.add(tab, text=tabs[i-1])
            tabs_ref.append(tab)
        
        top_bar = tk.Frame(self.root, height=50, bg='blue')
        top_bar.pack(fill=tk.X)
        tab_control.pack(fill=tk.Y, expand=True)
        
        profile_button = tk.Button(top_bar, text=' P ')
        profile_button.pack(side=tk.RIGHT)
        
        
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

        

        
        
        
    
        
        