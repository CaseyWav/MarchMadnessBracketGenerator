class team:
    def __init__(self, startingPos, name, seed, netRanking, rpi):
        
        #ex) Team 1
        self.startingPos = startingPos
        #ex) UConn
        self.name = name
        #ex) 1
        self.seed = seed
        #ex) 1-64
        self.netRanking = netRanking
        #ex) .566
        self.rpi = rpi

    def getName(self):
        return self.name
