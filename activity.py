class activity:
    def __init__(self, name, value, asignee, beneficiary, local, date, type='None', description = '', file=None):
        self.name = name
        self.value = value
        self.asignee = asignee
        self.beneficiary = beneficiary
        self.local = local
        self.date = date
        self.type = type
        self.description = description.replace('\n', ' ')
        self.file = file
        
    def register(self):
        with open('activities.txt', 'a') as f:
            f.write(f"{self.type}, {self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {self.local}, {self.date}, {self.description}, -\n")
