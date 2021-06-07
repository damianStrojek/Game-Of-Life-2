# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from random import randrange
from Plant import Plant

class Dandelion(Plant):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Dandelion, self).__init__(_currentWorld, _positionX, _positionY)
    
    def getName(self):
        return "Dandelion"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'dandelionhex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'dandelion.png'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def action(self):
        self.age += 1
        # Three tries to clone itself
        randomTick = [randrange(1,100,1), randrange(1,100,1), randrange(1,100,1)]
        for i in range(len(randomTick)):
            if randomTick[i] > 85:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + ") is sewing.")
                newPosition = self.findNewUnoccupiedField()

                if newPosition[0] == None or newPosition[1] == None:
                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) + ") failed sewing.")
                    return
                else:
                    self.clone(newPosition)

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Dandelion(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])
