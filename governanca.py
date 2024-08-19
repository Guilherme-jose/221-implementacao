class governanca:
    def __init__(self, tipo, consumo, local, gasto, type='None', file=None):
        self.tipo = tipo
        self.consumo = consumo
        self.local = local
        self.gasto = gasto
        self.type = type
        self.file = file
        
    def register(self):
        with open('governança.txt', 'a') as f:
            if self.file == None:
                f.write(f"{self.type}, {self.tipo}, {self.consumo}, {self.local}, {self.gasto}, {'-'}\n")
            else:
                f.write(f"{self.type}, {self.tipo}, {self.consumo}, {self.local}, {self.gasto}, {self.file.get_path()}\n")