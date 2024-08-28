import pytest
import tkinter as tk
from tkinter import ttk
from unittest.mock import Mock, patch
from social_tab import social_tab  

@pytest.fixture
def setup_tkinter():
    # Configura o ambiente Tkinter para o teste
    root = tk.Tk()
    tab_instance = social_tab(root)
    yield root, tab_instance
    root.destroy()

def test_social_tab_widgets(setup_tkinter):
    root, tab_instance = setup_tkinter

    # Substitua o método open_event_screen por um mock
    tab_instance.open_event_screen = Mock(name='open_event_screen')

    # Chama o método show para criar os widgets
    tab_instance.show()
    
    # Verifica se o label foi criado
    label = root.children.get('!label')  
    assert label is not None
    assert label.cget('text') == 'Social Tab'
    
    # Verifica se o botão foi criado
    button = root.children.get('!button') 
    assert button is not None
    assert button.cget('text') == 'Open Event Screen'

    # Testa se o comando do botão chama o método correto
    # Simula o clique do botão
    button.invoke()

    # Verifica se o método open_event_screen foi chamado
    tab_instance.open_event_screen.assert_called_once()

    # Verifica se a função display_activities foi chamada
    with patch.object(tab_instance, 'display_activities', autospec=True) as mock_display_activities:
        tab_instance.show()
        mock_display_activities.assert_called_once_with('social')
