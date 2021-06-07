# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from Animal import Animal

class Fox(Animal):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Fox, self).__init__(3, 7, _currentWorld, _positionX, _positionY)
    
    def getName(self):
        return "Fox"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'foxhex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'fox.png'))
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def action(self):
        self.age += 1
        if self.newBorn:
            self.newBorn = False
            return
        
        newPosition = self.findNewField()
        # Moveing only when we can fight another organism, else we don't move
        from Dirt import Dirt
        if newPosition[0] == None or newPosition[1] == None:
            # We don't move
            return
        elif isinstance(self.currentWorld.myMap[newPosition[0]][newPosition[1]], Dirt):
            self.setDirtOnMap()
            self.setPositionX(newPosition[0])
            self.setPositionY(newPosition[1])
            self.setMyselfOnMap()
        elif self.currentWorld.myMap[newPosition[0]][newPosition[1]].getStrength() < self.getStrength():
            self.collision(self.currentWorld.myMap[newPosition[0]][newPosition[1]])
        else:
            # We don't move
            return

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Fox(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])