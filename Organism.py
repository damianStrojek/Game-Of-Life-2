# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
from random import randrange

class Organism:
    age = 0                     # Age of the organism
    strength = None             # Strength of the organism
    initiative = None           # Initiative of the organism
    currentWorld = None         # World that organism is currently in
    positionX = None            # Position X (width)
    positionY = None            # Position Y (height)
    newBorn = False             # Is it new born or not
    image = None                # Picture of the organism
    isAlive = True              # Is organism alive (to remove it)
    cooldownToBreed = 3         # Time to the next breed, default is 3 rounds

    def __init__(self, _strength, _initiative, _currentWorld, _positionX, _positionY, _newBorn):
        self.age = 0
        self.strength = _strength
        self.initiative = _initiative
        self.currentWorld = _currentWorld
        self.positionX = _positionX
        self.positionY = _positionY
        self.newBorn = _newBorn
        self.isAlive = True
        self.cooldownToBreed = 0

    def action(self):
        pass

    def collision(self):
        pass

    def getImage(self):
        pass

    def clone(self, newPosition):
        pass

    def reflected(self, _collidingEntity):
        pass

    # GETTERS
    def getName(self):
        pass

    def getAge(self):
        return self.age

    def getStrength(self):
        return self.strength

    def getInitiative(self):
        return self.initiative

    def getX(self):
        return self.positionX
        
    def getY(self):
        return self.positionY

    def getNewBorn(self):
        return self.newBorn

    def getIsAlive(self):
        return self.isAlive

    def getOrganismToSave(self):
        # Getting organism information to save it to the file
        if self.getName() == "Human":
            toReturn = (self.getName() + " " + str(self.getAge()) + " " + \
            str(self.getX()) + " " + str(self.getY()) + " " + \
            str(self.getStrength()) + " " + str(self.getCooldownTime()))
        else:
            toReturn = (self.getName() + " " + str(self.getAge()) + " " + \
            str(self.getX()) + " " + str(self.getY()) + " " + \
            str(self.getStrength()))
        return toReturn

    # SETTERS
    def setAge(self, _age):
        self.age = _age

    def setStrength(self, _strength):
        self.strength += _strength

    def setStrengthTo(self, _strength):
        self.strength = _strength

    def setPositionX(self, _newPositionX):
        self.positionX = _newPositionX

    def setPositionY(self, _newPositionY):
        self.positionY = _newPositionY

    def setCooldownToBreed(self):
        self.cooldownToBreed = 3

    def died(self):
        self.isAlive = False
        self.currentWorld.addToRemove(self)

    def setDirtOnMap(self):
        from Dirt import Dirt
        self.currentWorld.myMap[self.getX()][self.getY()] = Dirt(self.currentWorld, self.getX(), self.getY())

    def setMyselfOnMap(self):
        self.currentWorld.myMap[self.getX()][self.getY()] = self

    def setMyselfOnPosition(self, newPosition):
        self.currentWorld.myMap[newPosition[0]][newPosition[1]] = self

    # Finding new position, it doesnt matter if it is taken
    def findNewField(self):
        returnPosition = [self.getX(), self.getY()]
        # Squared world
        if self.currentWorld.getWorldType() == 0:
            while True:
                field = randrange(4)
                # UP
                if field == 0:
                    if returnPosition[1]-1 != -1:
                        returnPosition[1] -= 1
                        return returnPosition
                # RIGHT
                elif field == 1:
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth():
                        returnPosition[0] += 1
                        return returnPosition
                # DOWN
                elif field == 2:
                    if returnPosition[1]+1 != self.currentWorld.getWorldHeight():
                        returnPosition[1] += 1
                        return returnPosition
                # LEFT
                elif field == 3:
                    if returnPosition[0]-1 != -1:
                        returnPosition[0] -= 1
                        return returnPosition
        # Hex world
        elif self.currentWorld.getWorldType() == 1:
            while True:
                field = randrange(6)
                # UP LEFT
                if field == 0:
                    if returnPosition[0]-1 != -1 and returnPosition[1]-1 != -1:
                        returnPosition[0] -= 1
                        returnPosition[1] -= 1
                        return returnPosition
                # UP RIGHT
                elif field == 1:
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                        returnPosition[1]-1 != -1:
                        returnPosition[0] += 1
                        returnPosition[1] -= 1
                        return returnPosition
                # RIGHT
                elif field == 2:
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth():
                        returnPosition[0] += 1
                        return returnPosition
                # DOWN RIGHT
                elif field == 3:
                    if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                        returnPosition[1]+1 != self.currentWorld.getWorldHeight():
                        returnPosition[0] += 1
                        returnPosition[1] += 1
                        return returnPosition
                # DOWN LEFT
                elif field == 4:
                    if returnPosition[0]-1 != -1 and \
                        returnPosition[1]+1 != self.currentWorld.getWorldHeight():
                        returnPosition[0] -= 1
                        returnPosition[1] += 1
                        return returnPosition
                # LEFT
                elif field == 5:
                    if returnPosition[0]-1 != -1:
                        returnPosition[0] -= 1
                        return returnPosition

    # Find new unoccupied field to breed
    def findNewUnoccupiedField(self):
        from Dirt import Dirt
        returnPosition = [self.getX(), self.getY()]
        if self.currentWorld.getWorldType() == 0:
            # UP
            if returnPosition[1]-1 != -1 and \
                isinstance(self.currentWorld.myMap[returnPosition[0]][returnPosition[1]-1], Dirt):
                returnPosition[1] -= 1
                return returnPosition
            # DOWN
            elif returnPosition[1]+1 != self.currentWorld.getWorldHeight() and \
                isinstance(self.currentWorld.myMap[returnPosition[0]][returnPosition[1]+1], Dirt):
                returnPosition[1] += 1
                return returnPosition
            # LEFT
            elif (returnPosition[0]-1) != -1 and \
                isinstance(self.currentWorld.myMap[returnPosition[0]-1][returnPosition[1]], Dirt):
                returnPosition[0] -= 1
                return returnPosition
            # RIGHT
            elif (returnPosition[0]+1) != self.currentWorld.getWorldWidth() and \
                isinstance(self.currentWorld.myMap[returnPosition[0]+1][returnPosition[1]], Dirt):
                returnPosition[0] += 1
                return returnPosition
            # If there is no unoccupied field around
            else:
                returnPosition[0] = None
                returnPosition[1] = None
                return returnPosition
        elif self.currentWorld.getWorldType() == 1:
            # UP LEFT
            if returnPosition[0]-1 != -1 and returnPosition[1]-1 != -1 and \
                isinstance(self.currentWorld.myMap[returnPosition[0]-1][returnPosition[1]-1], Dirt):
                returnPosition[0] -= 1
                returnPosition[1] -= 1
                return returnPosition
            # UP RIGHT
            if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                returnPosition[1]-1 != -1 and \
                isinstance(self.currentWorld.myMap[returnPosition[0]+1][returnPosition[1]-1], Dirt):
                returnPosition[0] += 1
                returnPosition[1] -= 1
                return returnPosition
            # RIGHT
            if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                isinstance(self.currentWorld.myMap[returnPosition[0]+1][returnPosition[1]], Dirt):
                returnPosition[0] += 1
                return returnPosition
            # DOWN RIGHT
            if returnPosition[0]+1 != self.currentWorld.getWorldWidth() and \
                returnPosition[1]+1 != self.currentWorld.getWorldHeight() and \
                isinstance(self.currentWorld.myMap[returnPosition[0]+1][returnPosition[1]+1], Dirt):
                returnPosition[0] += 1
                returnPosition[1] += 1
                return returnPosition
            # DOWN LEFT
            if returnPosition[0]-1 != -1 and \
                returnPosition[1]+1 != self.currentWorld.getWorldHeight() and \
                isinstance(self.currentWorld.myMap[returnPosition[0]-1][returnPosition[1]+1], Dirt):
                returnPosition[0] -= 1
                returnPosition[1] += 1
                return returnPosition
            # LEFT
            if not returnPosition[0]-1 != -1 and \
                isinstance(self.currentWorld.myMap[returnPosition[0]-1][returnPosition[1]], Dirt):
                returnPosition[0] -= 1
                return returnPosition
            # IF THERE IS NOTHING LEFT
            else:
                returnPosition[0] = None
                returnPosition[1] = None
                return returnPosition