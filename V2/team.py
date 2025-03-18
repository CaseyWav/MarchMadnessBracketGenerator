class team:
    def __init__(self, startingPos, name, seed):
        
        #ex) Team 1
        self.startingPos = startingPos
        #ex) UConn
        self.name = name
        #ex) 1
        self.seed = seed

    def getName(self):
        return self.name
