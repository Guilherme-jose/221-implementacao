class activity:
    def __init__(self, name, value, asignee, beneficiary, file=None):
        self.name = name
        self.value = value
        self.asignee = asignee
        self.beneficiary = beneficiary
        self.file = file
        
    def register(self):
        with open('activities.txt', 'a') as f:
            if self.file == None:
                f.write(f"{self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {'-'}\n")
            else:
                f.write(f"{self.name}, {self.value}, {self.asignee}, {self.beneficiary}, {self.file.get_path()}\n")