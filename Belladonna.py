# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from Plant import Plant

class Belladonna(Plant):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Belladonna, self).__init__(_currentWorld, _positionX, _positionY)
        self.setStrength(99)
        self.image = pygame.image.load(os.path.join('icons', 'belladonna.png'))
    
    def getName(self):
        return "Belladonna"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'belladonnahex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'belladonna.png'))
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Belladonna(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])