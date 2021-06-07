# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
from random import randrange
from Organism import Organism

class Plant(Organism):
    def __init__(self, _currentWorld=None, _positionX=None, _positionY=None):
        super().__init__(0, 0, _currentWorld, _positionX, _positionY, False)

    def action(self):
        # Every round adds +1 to the age
        self.age += 1
        # Plants dont breed, they clone themselves and have 15% to do it
        randomTick = randrange(1, 100, 1)
        if randomTick > 85:
            self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + \
            "," + str(self.getY()+1) + ") is sewing.")
            
            newPosition = self.findNewUnoccupiedField()
            if newPosition[0] == None or newPosition[1] == None:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + \
                "," + str(self.getY()+1) + ") failed sewing.")
                return
            else:
                self.clone(newPosition)
