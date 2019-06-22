##initialize player if no player is selected at first
##load player if selected

class Model():
    def __init__(self, status):
      # if status is given, take that status
      if(status):
        self.status = status
      # if is NOT given, initialize the status with random value within range
      else:
        self.status = {}
        self.money = 0
        self.items = []

class Player(Model):
    def __init__(self, status):
        pass
    def lvlup():
        pass
    def getStatus():
        pass
    def healHp():
        pass
    
    
class Enemy(Model):
    def __init__(self, phase):
        ##phaseが増えるにつれ強くする

