# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os
from Animal import Animal

class Cybersheep(Animal):
    def __init__(self, _currentWorld, _positionX, _positionY):
        super(Cybersheep, self).__init__(11, 4, _currentWorld, _positionX, _positionY)

    def getName(self):
        return "Cybersheep"

    def action(self):
        self.age += 1
        if self.cooldownToBreed > 0:
            self.cooldownToBreed -= 1

        if self.newBorn:
            self.newBorn = False
        else:
            # How many hogweeds are on the map
            countOfHogweed = self.currentWorld.howManyOrganisms("Hogweed")
            # If there is any hogweed we look for it
            from Dirt import Dirt
            if countOfHogweed > 0:
                # We look for the closest hogweed to our organism
                destinationHogweed = self.currentWorld.closestHogweed(self)
                # And we calculate our next position so we are closer to the closes hogweed
                newPosition = self.currentWorld.findPathToDestination(self, destinationHogweed)
                # If it is dirt we move there instantly
                if isinstance(self.currentWorld.myMap[newPosition[0]][newPosition[1]], Dirt):
                    self.setDirtOnMap()
                    self.setPositionX(newPosition[0])
                    self.setPositionY(newPosition[1])
                    self.setMyselfOnMap()
                # Else we collide with this organism because it's on our way
                else:
                    self.currentWorld.log(self.getName() + " at (" + str(self.getX()+1) + "," + str(self.getY()+1) +\
                    ") collided with " + self.currentWorld.myMap[newPosition[0]][newPosition[1]].getName() + " at (" +\
                    str(newPosition[0]+1) + "," + str(newPosition[1]+1) + ").")

                    self.collision(self.currentWorld.myMap[newPosition[0]][newPosition[1]])
            else:
                # Normal sheep action
                newPosition = self.findNewField()
                if isinstance(self.currentWorld.myMap[newPosition[0]][newPosition[1]], Dirt):
                    self.setDirtOnMap()
                    self.setPositionX(newPosition[0])
                    self.setPositionY(newPosition[1])
                    self.setMyselfOnMap()
                else:
                    self.collision(self.currentWorld.myMap[newPosition[0]][newPosition[1]])

    def getImage(self):
        if self.currentWorld.getWorldType() == 1:
            self.image = pygame.image.load(os.path.join('icons', 'cyberSheephex.jpg'))
        else:
            self.image = pygame.image.load(os.path.join('icons', 'cyberSheep.png'))
        self.image = pygame.transform.scale(self.image, (self.currentWorld.getIconWidth(), self.currentWorld.getIconHeight()))
        return self.image

    def clone(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = Cybersheep(self.currentWorld, newPosition[0], newPosition[1])
        self.currentWorld.addToAdd(self.currentWorld.myMap[newPosition[0]][newPosition[1]])