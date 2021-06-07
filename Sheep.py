# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from Animal import Animal

class Sheep(Animal):
    def __init__(self, _currentWorld=None, _positionX=None, _positionY=None):
        super(Sheep, self).__init__(4, 4, _currentWorld, _positionX, _positionY)
    
    def getName(self):
        return "Sheep"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'sheephex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'sheep.png'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Sheep(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])