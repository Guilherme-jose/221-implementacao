from tab import tab
from tkinter import ttk
from fpdf import FPDF
import json

class relatorio_tab(tab):
    def __init__(self, root):
        self.root = root
        
    def show(self):
        gerar_relatorio_button = ttk.Button(self.root, text="Gerar Relatório", command=self.gerar_relatorio)
        gerar_relatorio_button.pack()
        

    def gerar_relatorio(self):
        with open('activities.json', 'r', encoding='utf-8') as f:
            activities = json.loads(f.read())

        pdf = FPDF()

        pdf.set_title('Relatório de Atividades')
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Relatório de Atividades', ln=True, align='C')

        pdf.set_font('Arial', '', 12)
        for activity in activities:
            if activity['type'] == 'social' or activity['type'] == 'ambiente' or activity['type'] == 'governanca':
                pdf.multi_cell(0, 10, f'{list(activity.values())}')

        pdf.output('relatorio.pdf')