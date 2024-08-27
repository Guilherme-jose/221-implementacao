import pytest
import tkinter as tk
from tkinter import ttk
from main_tab import main_tab  

@pytest.fixture
def setup_tkinter():
    root = tk.Tk()
    yield root
    root.destroy()

def test_show_creates_label(setup_tkinter):
    root = setup_tkinter
    tab_instance = main_tab(root)
    tab_instance.show()
    
    label = root.children.get('!label')
    assert label is not None
    assert isinstance(label, ttk.Label)
    assert label.cget('text') == 'Main Tab'
