class gastos:
    def __init__(self, consumo, mes, type='None', file=None):
        self.consumo = consumo
        self.mes = mes
        self.type = type
        self.file = file
        
    def register(self):
        with open('gastos.txt', 'a') as f:
            if self.file == None:
                f.write(f"{self.type}, {self.consumo}, {self.mes}, {'-'}\n")
            else:
                f.write(f"{self.type}, {self.consumo}, {self.mes}, {self.file.get_path()}\n")