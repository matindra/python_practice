class Patient():

    def __init__(self, name, disease, age, place):
        self.name = name
        self.disease = disease
        self.age = age
        self.place = place
    
    def Under_Treatment(self):
        print('Patient ', self.name, ' is under treatment')

    def Discharged(self):
        print('Patient ', self.name, ' is discharged')

patient1 = Patient('Raghua', 'fever', 25, 'bhadrak')
patient2 = Patient('Hari', 'corona', 30, 'bbsr')

print(patient1.name)
patient1.Under_Treatment()

print(patient2.name, ' having ', patient2.disease, 'aged', patient2.age, ' years \n''is from ', patient2.place, ' district ')
