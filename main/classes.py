class Player:
    def __init__(self, name, age): #age?
        self.name = name
        self.age : int = age

class Creature:
    def __init__(self, name, skills1, successRate):
        self.name = name
        self.skills1 = skills1
        self.successRate = successRate
    def calculation(self, skills1):
        if "Horse" in skills1 and "Flight" in skills1:
            self.successRate += 11
    def failRate(self, successRate):
        if successRate < 10:
            return "Your species will not survive under its current conditions"
        elif successRate > 10:
            return "Your species will survive"
