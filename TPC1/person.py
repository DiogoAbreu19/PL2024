class Person:
    def __init__(self, values):
        self.id = values[0]
        self.index = values[1]
        self.emdDate = values[2]
        self.firstName = values[3]
        self.lastName = values[4]
        self.age = int(values[5])
        self.gender = values[6]
        self.address = values[7]
        self.modality = values[8]
        self.club = values[9]
        self.email = values[10]
        self.federate = values[11]
        self.result = values[12]

    def isFit(self):
        return self.result
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getAge(self):
        return self.age
    
    def __str__(self):
        return f'Name: {self.getFirstName()} {self.getLastName()} | Age: {self.getAge()}' 