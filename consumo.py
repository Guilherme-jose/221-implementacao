class consumo:
    def __init__(self, consumos, periodo, type='None', file=None):
        self.consumos = consumos
        self.periodo = periodo
        self.type = type
        self.file = file
        
    def register(self):
        with open('activities.txt', 'a') as f:
            if self.file == None:
                f.write(f"{self.type}, {self.consumos}, {self.periodo}, {'-'}\n")
            else:
                f.write(f"{self.type}, {self.consumos}, {self.periodo}, {self.file}\n")