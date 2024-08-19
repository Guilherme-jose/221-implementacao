class activity:
    def __init__(self, name, value, asignee, beneficiary, local, date, type='None', file=None):
        self.name = name
        self.value = value
        self.asignee = asignee
        self.beneficiary = beneficiary
        self.local = local
        self.date = date
        self.type = type
        self.file = file
        
    def register(self):
        with open('activities.txt', 'a') as f:
            if self.file == None:
                f.write(f"{self.type}, {self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {self.local}, {self.date}, {'-'}\n")
            else:
                f.write(f"{self.type}, {self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {self.local}, {self.date}, {self.file.get_path()}\n")