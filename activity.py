import json

class activity:
    def __init__(self, name, value, asignee, beneficiary, local, date, type='None', description = '', file=[], account=None):
        self.name = name
        self.value = value
        self.asignee = asignee
        self.beneficiary = beneficiary
        self.local = local
        self.date = date
        self.type = type
        self.description = description
        self.file = file
        self.account = account
        
    def register(self):
        with open('activities.json', 'r', encoding='utf-8') as f:
            activities = json.loads(f.read())
            activities.append({'type': self.type, 'name': self.name, 'value': self.value, 'asignee': self.asignee, 'beneficiary': self.beneficiary, 'local': self.local, 'date': self.date, 'description': self.description, 'file': self.file, 'account': self.account})
            
        with open('activities.json', 'w+', encoding='utf-8') as f:
            f.write(json.dumps(activities, indent=True))
    