# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from random import randrange
from Animal import Animal

class Turtle(Animal):
    def __init__(self, _currentWorld=None, _positionX=None, _positionY=None):
        super(Turtle, self).__init__(2, 1, _currentWorld, _positionX, _positionY)

    def getName(self):
        return "Turtle"

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'turtlehex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'turtle.png'))
            
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image
    
    def action(self):
        self.age += 1
        if self.cooldownToBreed > 0:
            self.cooldownToBreed -= 1
        # Turtle has only 25% chance to move to the new position
        tickRate = randrange(4)
        if self.newBorn:
            self.newBorn = False
        elif tickRate == 0:
            newPosition = self.findNewField()
            from Dirt import Dirt
            if isinstance(self.currentWorld.myMap[newPosition[0]][newPosition[1]], Dirt):
                if newPosition[0] != None and newPosition[1] != None:
                    self.setDirtOnMap()
                    self.setPositionX(newPosition[0])
                    self.setPositionY(newPosition[0])
                    self.setMyselfOnMap()
            else:
                self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) +\
                ") collided with " + self.currentWorld.myMap[newPosition[0]][newPosition[1]].getName() + " at (" +\
                str(newPosition[0]+1) + "," + str(newPosition[1]+1) + ").")

                self.collision(self.currentWorld.myMap[newPosition[0]][newPosition[1]])

    def reflected(self, _collidingEntity):
        # If colliding entity strength is lower than 5 turtle will always reflect this attack
        if _collidingEntity.getStrength() < 5:
            return True
        else:
            return False
    
    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Turtle(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])