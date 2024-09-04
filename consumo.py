import json

class consumo:
    def __init__(self, consumos, periodo, type='None', file=None):
        self.consumos = consumos
        self.periodo = periodo
        self.type = type
        self.file = file
        
    def register(self):
        with open('activities.json', 'r', encoding='utf-8') as f:
            activities = json.loads(f.read())
            if self.file == None:
                activities.append({'type': self.type, 'consumos': self.consumos, 'periodo': self.periodo, 'file': '-'})
            else:
                activities.append({'type': self.type, 'consumos': self.consumos, 'periodo': self.periodo, 'file': self.file})
            
            activities.append({'type': self.type, 'name': self.name, 'value': self.value, 'asignee': self.asignee, 'beneficiary': self.beneficiary, 'local': self.local, 'date': self.date, 'description': self.description, 'file': self.file})
            
        with open('activities.json', 'w+', encoding='utf-8') as f:
            f.write(json.dumps(activities, indent=True))