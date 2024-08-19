class activity:
    def __init__(self, name, value, asignee, beneficiary, type='None', description = '', file=None):
        self.name = name
        self.value = value
        self.asignee = asignee
        self.beneficiary = beneficiary
        self.type = type
        self.description = description
        self.file = file
        
    def register(self):
        with open('activities.txt', 'a') as f:
            if self.file == None:
                f.write(f"{self.type}, {self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {self.description}, {'-'.encode('utf-8')}\n")
            else:
                f.write(f"{self.type}, {self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {self.description}, {self.file.get_path()}\n")