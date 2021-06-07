# OOP PG WETI PROJECT NR 2
# Damian Strojek s184407 2021 IT/CS
# @ Copyright 2021, Damian Strojek, All rights reserved.
import pygame, os, math
from random import randrange
from Dirt import Dirt

class World:
    ICONWIDTH, ICONHEIGHT = 19, 19                      # Icon size
    backgroundColor = (255, 255, 255)                   # Background color of map
    typeOfWorld = 0                                     # 0 - Square world, 1 - Hex world
    round = 0                                           # Which round
    worldWidth = None                                   # World size of X axis
    worldHeight = None                                  # World size of Y axis
    widthOfLegend = 60                                  # Size [px] of legend to the left
    sizeOfNumber = 20                                   # Size [px] of numbers around
    organisms = []                                      # Table with alive organisms
    toAdd = []                                          # Table with organisms to add
    toRemove = []                                       # Table with organisms to remove
    logs = []                                           # Logs of every round
    myHuman = None                                      # Pointer to our human
    myMap = None                                        # 3D array of positions on map
    lastClick = False                                   # Flag if out last mouse click was in bounds
    lastPositionToSpawn = []                            # Last position that was clicked on and was in bounds

    def __init__(self, _worldWidth, _worldHeight):
        from Human import Human
        self.worldWidth = _worldWidth
        self.worldHeight = _worldHeight
        self.myHuman = Human(self, None, None)
        self.myMap = [[Dirt(self, y, x) for x in range(self.worldHeight)] for y in range(self.worldWidth)]

    # GETTERS
    def getIconWidth(self):
        return self.ICONWIDTH

    def getIconHeight(self):
        return self.ICONHEIGHT

    def getWorldType(self):
        return self.typeOfWorld

    def getWorldWidth(self):
        return self.worldWidth

    def getWorldHeight(self):
        return self.worldHeight

    def getHeightMargin(self):
        # Margin of numbers up and info below
        return (self.sizeOfNumber+35)

    def getNumber(self):
        return self.sizeOfNumber

    def getWidthMargin(self):
        # Margin of legend and numbers
        return (self.widthOfLegend+self.sizeOfNumber)

    def getRound(self):
        return self.round

    def getLastClick(self):
        return self.lastClick

    def clearCmd(self):
        os.system("cls")

    # FUNCTIONS
    def drawWindow(self, WIN):
        WIN.fill(self.backgroundColor)

        if self.getWorldType() == 0:
            for i in range(self.worldHeight):
                for j in range(self.worldWidth):
                    WIN.blit(self.myMap[j][i].getImage(), (self.myMap[j][i].getX()*20, self.myMap[j][i].getY()*20))
        elif self.getWorldType() == 1:
            for i in range(self.worldHeight):
                for j in range(self.worldWidth):
                    if i % 2 == 0:
                        WIN.blit(self.myMap[j][i].getImage(), (self.myMap[j][i].getX()*20+20, self.myMap[j][i].getY()*20))
                    else:
                        WIN.blit(self.myMap[j][i].getImage(), (self.myMap[j][i].getX()*20+10, self.myMap[j][i].getY()*20))

        self.drawLegend(WIN)
        self.drawNumbers(WIN)
        self.drawInfo(WIN)
        self.clearCmd()
        print("Logs of " + str(self.getRound()+1) + " round :")
        for i in range(len(self.logs)):
            print(self.logs[i])

        # Game over
        if not self.myHuman.getIsAlive():
            gameOverFont = pygame.font.SysFont('comicsans', 50)
            gameOverText = gameOverFont.render("GAME OVER", False, (0,0,0))
            WIN.blit(gameOverText, ((self.getWorldWidth()*20+self.getWidthMargin())//2, (self.getWorldHeight()*20+self.getHeightMargin())//2))

        # Updating the display
        pygame.display.update()

    def drawLegend(self, WIN):
        tableOfNames = ["Antelope", "Belladonna", "Cybersheep", "Dandelion", "Dirt", "Fox", "Grass", \
        "Guarana", "Hogweed", "Human", "Sheep", "Turtle", "Wolf"]
        if self.getWorldType() == 0:
            tableOfImages = ["antelope.png", "belladonna.png", "cyberSheep.png", "dandelion.png", "dirt.jpg", \
            "fox.png", "grass.jpg", "guarana.png", "hogweed.png", "human.jpg", "sheep.png", \
            "turtle.png", "wolf.png"]
            for i in range(len(tableOfImages)):
                image = pygame.transform.scale(pygame.image.load(os.path.join('icons', tableOfImages[i])), \
                (self.getIconWidth(), self.getIconHeight()))
                text = pygame.font.SysFont('arial', 10).render(tableOfNames[i], False, (0, 0, 0))
                WIN.blit(image, (self.getWorldWidth()*20+self.getNumber()+20, i*32+3))
                WIN.blit(text, (self.getWorldWidth()*20+self.getNumber()+10, i*32+23))
        elif self.getWorldType() == 1:
            tableOfImagesHex = ["antelopehex.jpg", "belladonnahex.jpg", "cyberSheephex.jpg", "dandelionhex.jpg", "dirthex.jpg", \
            "foxhex.jpg", "grasshex.jpg", "guaranahex.jpg", "hogweedhex.jpg", "humanhex.jpg", "sheephex.jpg", \
            "turtlehex.jpg", "wolfhex.jpg"]
            for i in range(len(tableOfImagesHex)):
                image = pygame.transform.scale(pygame.image.load(os.path.join('icons', tableOfImagesHex[i])), \
                (self.getIconWidth(), self.getIconHeight()))
                text = pygame.font.SysFont('arial', 10).render(tableOfNames[i], False, (0, 0, 0))
                WIN.blit(image, (self.getWorldWidth()*20+self.getNumber()+40, i*32+3))
                WIN.blit(text, (self.getWorldWidth()*20+self.getNumber()+30, i*32+23))

    def drawNumbers(self, WIN):
        numbersFont = pygame.font.SysFont('comicsan', 20)
        if self.getWorldType() == 0:
            for i in range(self.getWorldHeight()):
                WIN.blit(numbersFont.render(str(i+1), False, (0, 0, 0)), (self.getWorldWidth()*20+5, i*20+4))
                WIN.blit(numbersFont.render(str(i+1), False, (0, 0, 0)), (i*20+5, self.getWorldHeight()*20+4))
        elif self.getWorldType() == 1:
            for i in range(self.getWorldHeight()):
                WIN.blit(numbersFont.render(str(i+1), False, (0, 0, 0)), (self.getWorldWidth()*20+25, i*20+4))
                WIN.blit(numbersFont.render(str(i+1), False, (0, 0, 0)), (i*20+5+10, self.getWorldHeight()*20+4))

    def drawInfo(self, WIN):
        strengthText = pygame.font.SysFont('comicsans', 40).render("Strength: " + \
        str(self.myHuman.getStrength()), False, (0, 0, 0))
        roundText = pygame.font.SysFont('comicsans', 40).render("Round: " + \
        str(self.getRound()), False, (0, 0, 0))
        image = pygame.transform.scale(pygame.image.load(os.path.join('icons', 'obsidianhex.jpg')), \
        (30, 30))
        if self.getWorldType() == 1:
            image = pygame.transform.scale(pygame.image.load(os.path.join('icons', 'obsidian.png')), \
            (25, 25))
            WIN.blit(image, (self.getWorldWidth()*20+self.getNumber()+35, 13*32+3))
        else:
            WIN.blit(image, (self.getWorldWidth()*20+self.getNumber()+20, 13*32+3))
        WIN.blit(roundText, (10, self.getWorldHeight()*20+5+self.getNumber()))
        WIN.blit(strengthText, (160, self.getWorldHeight()*20+5+self.getNumber()))
        
    def placeRandom(self, _organism):
        # Randomly place our start organisms
        flag = True
        while flag:
            randomX = randrange(self.worldWidth)
            randomY = randrange(self.worldHeight)
            
            if isinstance(self.myMap[randomX][randomY], Dirt):
                self.myMap[randomX][randomY] = _organism
                _organism.setPositionX(randomX)
                _organism.setPositionY(randomY)
                self.addToAdd(_organism)
                flag = False

    def howManyOrganisms(self, organismName):
        j = 0
        for i in range(len(self.organisms)):
            if self.organisms[i].getName() == organismName:
                j += 1
        return j
    
    def closestHogweed(self, _organism):
        # Search for all hogweeds in the map
        hogweeds = []
        for i in range(len(self.organisms)):
            if self.organisms[i].getName() == "Hogweed":
                hogweeds.append(self.organisms[i])
        # Calculate distances to the hogweeds
        distances = []
        for i in range(len(hogweeds)):
            distances.append(math.sqrt(math.pow(hogweeds[i].getX()-_organism.getX(), 2) + math.pow(hogweeds[i].getY()-_organism.getY(), 2)))
        # Search for the closest distance
        lowestDistance = 100
        lowestIndex = 0
        for i in range(len(distances)):
            if distances[i] < lowestDistance:
                lowestDistance = distances[i]
                lowestIndex = i
        # Return closes hogweed to _organism
        return hogweeds[lowestIndex]

    def findPathToDestination(self, sourceOrganism, destinationOrganism):
        # This function returns newPosition that organism has to move to be closer to the destination Organism
        # It doesnt matter if it is occupied
        returnPosition = [sourceOrganism.getX(), sourceOrganism.getY()]
        # If X's are the same we need to change Y of source organism
        # or if Y's are not the same
        if returnPosition[0] == destinationOrganism.getX() or \
            returnPosition[1] != destinationOrganism.getY():
            if returnPosition[1] > destinationOrganism.getY():
                # We dont have to check all positions because there is already organism on that axis
                returnPosition[1] -= 1
            elif returnPosition[1] < destinationOrganism.getY():
                returnPosition[1] += 1
        # If Y's are the same we need to change X of source organism
        # or if X's are not the same
        elif returnPosition[1] == destinationOrganism.getY() or \
            returnPosition[0] != destinationOrganism.getX():
            if returnPosition[0] > destinationOrganism.getX():
                returnPosition[0] -= 1
            elif returnPosition[0] < destinationOrganism.getX():
                returnPosition[0] += 1
        return returnPosition

    def startGame(self):
        from Sheep import Sheep
        from Cybersheep import Cybersheep
        from Wolf import Wolf
        from Fox import Fox
        from Turtle import Turtle
        from Antelope import Antelope
        from Grass import Grass
        from Guarana import Guarana
        from Dandelion import Dandelion
        from Hogweed import Hogweed
        from Belladonna import Belladonna
        self.placeRandom(self.myHuman)

        self.placeRandom(Sheep(self, None, None))
        self.placeRandom(Sheep(self, None, None))

        self.placeRandom(Cybersheep(self, None, None))
        self.placeRandom(Cybersheep(self, None, None))

        self.placeRandom(Wolf(self, None, None))   
        self.placeRandom(Wolf(self, None, None)) 

        self.placeRandom(Fox(self, None, None))
        self.placeRandom(Fox(self, None, None))

        self.placeRandom(Turtle(self, None, None))
        self.placeRandom(Turtle(self, None, None))
        
        self.placeRandom(Antelope(self, None, None))
        self.placeRandom(Antelope(self, None, None))

        self.placeRandom(Grass(self, None, None))
        self.placeRandom(Guarana(self, None, None))
        self.placeRandom(Dandelion(self, None, None))
        self.placeRandom(Hogweed(self, None, None))
        self.placeRandom(Belladonna(self, None, None))

        self.addToOrganisms()

    def addToAdd(self, _organism):
        # Add organisms to add them to the game later
        self.toAdd.append(_organism)

    def addToOrganisms(self):
        # Adding new organisms to the map
        for i in range(len(self.toAdd)):
            self.organisms.append(self.toAdd[i])
        self.toAdd = []
        # Sorting organisms by their initiative
        self.organisms.sort(key=lambda organism: organism.getInitiative(), reverse=True)

    def addToRemove(self, _organism):
        # Add organisms to remove them from the game later
        self.toRemove.append(_organism)

    def removeOrganisms(self):
        # Removing organisms from the game
        for i in range(len(self.toRemove)):
            self.organisms.remove(self.toRemove[i])
        self.toRemove = []

    def log(self, logsAdd):
        # All logs of current round
        self.logs.append(logsAdd)

    def nextRound(self):
        # Action of every organism, they are already sorted
        j = len(self.organisms)
        for i in range(j):
            if self.organisms[i].getIsAlive():
                self.organisms[i].action()
        # Adding and removing organisms
        self.addToOrganisms()
        self.removeOrganisms()
        self.round += 1

    def clear(self):
        self.logs = []
        self.organisms = []
        self.toAdd = []
        self.toRemove = []
        self.myMap = [[Dirt(self, y, x) for x in range(self.worldHeight)] for y in range(self.worldWidth)]

    def saveWorld(self):
        # Default settings
        file = open("savedWorld.txt", "w")
        file.write("World " + str(self.getWorldWidth()) + " " + \
        str(self.getWorldHeight()) + " " + str(self.getRound()) + \
        " " + str(self.getWorldType()) + "\n")
        # All organisms alive
        for i in range(len(self.organisms)):
            file.write(self.organisms[i].getOrganismToSave() + "\n")
        file.close()

    def loadWorld(self):
        # Clearing old world
        self.clear()
        file = open("savedWorld.txt", "r")
        # Iterating through every line and adding new organism
        for line in file:
            words = line.split()
            if words[0] == "World":
                self.worldWidth = int(words[1])
                self.worldHeight = int(words[2])
                self.round = int(words[3])
                self.typeOfWorld = int(words[4])
            elif words[0] == "Antelope":
                from Antelope import Antelope
                self.myMap[int(words[2])][int(words[3])] = Antelope(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Belladonna":
                from Belladonna import Belladonna
                self.myMap[int(words[2])][int(words[3])] = Belladonna(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Cybersheep":
                from Cybersheep import Cybersheep
                self.myMap[int(words[2])][int(words[3])] = Cybersheep(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Dandelion":
                from Dandelion import Dandelion
                self.myMap[int(words[2])][int(words[3])] = Dandelion(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Fox":
                from Fox import Fox
                self.myMap[int(words[2])][int(words[3])] = Fox(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Grass":
                from Grass import Grass
                self.myMap[int(words[2])][int(words[3])] = Grass(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Guarana":
                from Guarana import Guarana
                self.myMap[int(words[2])][int(words[3])] = Guarana(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Hogweed":
                from Hogweed import Hogweed
                self.myMap[int(words[2])][int(words[3])] = Hogweed(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Human":
                from Human import Human
                self.myMap[int(words[2])][int(words[3])] = Human(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.myMap[int(words[2])][int(words[3])].setCooldownTimeTo(int(words[5]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
                self.myHuman = self.myMap[int(words[2])][int(words[3])]
            elif words[0] == "Sheep":
                from Sheep import Sheep
                self.myMap[int(words[2])][int(words[3])] = Sheep(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Turtle":
                from Turtle import Turtle
                self.myMap[int(words[2])][int(words[3])] = Turtle(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])
            elif words[0] == "Wolf":
                from Wolf import Wolf
                self.myMap[int(words[2])][int(words[3])] = Wolf(self, int(words[2]), int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setPositionX(int(words[2]))
                self.myMap[int(words[2])][int(words[3])].setPositionY(int(words[3]))
                self.myMap[int(words[2])][int(words[3])].setAge(int(words[1]))
                self.myMap[int(words[2])][int(words[3])].setStrengthTo(int(words[4]))
                self.addToAdd(self.myMap[int(words[2])][int(words[3])])

    def gameOver(self, WIN):
        # Game over notification
        gameOverFont = pygame.font.SysFont('comicsans', 50)
        gameOverText = gameOverFont.render("GAME OVER", False, (0,0,0))
        WIN.blit(gameOverText, ((self.getWorldWidth()*20+self.getWidthMargin())//2, \
        (self.getWorldHeight()*20+self.getHeightMargin())//2))
        pygame.time.wait(5000)

    def handleMouse(self, pos):
        # This function checks if our mouse was on Dirt (the rule is we can't spawn anything
        # on taken field)
        if self.getWorldType() == 0:
            self.lastPositionToSpawn = [math.floor(pos[0]//20), math.floor(pos[1]//20)]
            if isinstance(self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]], Dirt):
                self.log("You've chosen field (" + str(self.lastPositionToSpawn[0]+1) + "," + \
                str(self.lastPositionToSpawn[1]+1) + "). Choose organism.")
                self.lastClick = True
            else:
                self.lastPositionToSpawn = []
                self.lastClick = False
        elif self.getWorldType() == 1:
            self.lastPositionToSpawn = [math.floor(pos[0]//20), math.floor(pos[1]//20)]
            if self.lastPositionToSpawn[1] % 2 == 0:
                self.lastPositionToSpawn[0] -= 1

            if isinstance(self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]], Dirt):
                self.log("You've chosen field (" + str(self.lastPositionToSpawn[0]+1) + "," + \
                str(self.lastPositionToSpawn[1]+1) + "). Choose organism.")
                self.lastClick = True
            else:
                self.lastPositionToSpawn = []
                self.lastClick = False

    def setLastClick(self):
        self.lastClick = False

    def addClickedOrganism(self, pos):
        # If user clicked in legend's row
        if (pos[0] >= self.getWorldWidth()*20+self.getNumber()+20 and \
            pos[0] <= self.getWorldWidth()*20+self.getNumber()+40) or \
            pos[0] >= self.getWorldWidth()*20+self.getNumber()+40 and \
            pos[0] <= self.getWorldWidth()*20+self.getNumber()+60:
            # If user clicked or organism head we check for this head
            for i in range(13):
                if pos[1] >= i*32+3 and pos[1] <= i*32+22:
                    if i == 0:
                        from Antelope import Antelope
                        newOrganism = Antelope(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 1:
                        from Belladonna import Belladonna
                        newOrganism = Belladonna(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 2:
                        from Cybersheep import Cybersheep
                        newOrganism = Cybersheep(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 3:
                        from Dandelion import Dandelion
                        newOrganism = Dandelion(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 4:
                        self.log("You can't spawn Dirt on Dirt.")
                        break
                    elif i == 5:
                        from Fox import Fox
                        newOrganism = Fox(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 6:
                        from Grass import Grass
                        newOrganism = Grass(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 7:
                        from Guarana import Guarana
                        newOrganism = Guarana(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 8:
                        from Hogweed import Hogweed
                        newOrganism = Hogweed(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 9:
                        self.log("There cannot be 2 humans.")
                        break
                    elif i == 10:
                        from Sheep import Sheep
                        newOrganism = Sheep(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 11:
                        from Turtle import Turtle
                        newOrganism = Turtle(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
                    elif i == 12:
                        from Wolf import Wolf
                        newOrganism = Wolf(self, self.lastPositionToSpawn[0], self.lastPositionToSpawn[1])
                        self.myMap[self.lastPositionToSpawn[0]][self.lastPositionToSpawn[1]] = newOrganism
                        self.addToAdd(newOrganism)
                        self.log("You created " + newOrganism.getName() + " at field (" + str(newOrganism.getX()+1) + \
                        "," + str(newOrganism.getY()+1) + ").")
                        break
            self.addToOrganisms()
            self.lastClick = False
        else:
            self.lastClick = False
            return

    def handleChangeTheWorldType(self, pos, WIN):
        # Position of our button, its always in this position
        if pos[1] >= 13*32+3 and pos[1] <= 13*32+33:
            if self.typeOfWorld == 0:
                self.typeOfWorld = 1
                WIN = pygame.display.set_mode((self.getWorldWidth()*20+self.getWidthMargin()+20, \
                self.getWorldHeight()*20+self.getHeightMargin()))
            else:
                self.typeOfWorld = 0
                WIN = pygame.display.set_mode((self.getWorldWidth()*20+self.getWidthMargin(), \
                self.getWorldHeight()*20+self.getHeightMargin()))
