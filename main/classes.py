class Player:
    def __init__(self, name, age): #age?
        self.name = name
        self.age : int = age

class Creature:
    def __init__(self, name, skills, successRate=0):
        self.name = name
        self.skills = skills
        self.successRate : int = successRate
    def failRate(self, successRate):
        if self.successRate < 10:
            return "Your species will not survive under its current conditions"
        elif self.successRate > 10:
            return "Your species will survive"

