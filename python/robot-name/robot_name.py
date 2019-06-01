import string, random

class Robot(object):
    def __init__(self):
        self.previousNames = set()
        self.name = self.generateNewName()

    def generateNewName(self):
        isValidName = False
        while isValidName == False:
            name = ''
            for letterIdx in range(2):
                name+= random.choice(string.ascii_uppercase)
            for intIdx in range(3):
                name+= str(random.randint(0, 10))
            if name not in self.previousNames:
                self.previousNames.add(name)
                isValidName = True
        return name

    def reset(self):
        self.name = self.generateNewName()