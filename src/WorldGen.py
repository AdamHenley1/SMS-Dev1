## We need a lot of maths for this generation
from math import *
from random import *


## s is shovel, p is pickaxe
class Block:
    def __init__(self, x, y, name = "Dirt", move = True, info = "ms"):
        self.name = name
        self.move = move
        self.info = info
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return(self.name)

    def setBlock(self, name, move, info) -> None:
        self.name = name
        self.move = move
        self.info = info

    def setStone(self) -> None:
        self.setBlock("Stone", True, "mp")

    def setWWall(self) -> None:
        self.setBlock("W-Wall", False, "ma")

    def setWater(self) -> None:
        self.setBlock("Water", False, "f,d")

    def setTree(self) -> None:
        self.setBlock("Tree", False, "ma")

    def getProperties(self) -> int:
        return(0)

    def interact(self) -> None:
        return(None)

    
## Specific class for trees.
class Tree(Block):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, "Tree", False, "ma")

    def interact(self) -> int:
        return("td", randint(5,20))
        
        
## A class for the world.
## This goes y/x, not x/y as everything else
## in the known universe does.
class World:
    def __init__(self, name, sizeX = 4, sizeY = 4) -> None:
        self.ID = name
        self.size = (sizeX, sizeY)
        self.worldMap = []

    def __str__(self) -> str:
        retVal = ""
        for y in range(self.getY()):
            for x in range(self.getX()):
                retVal += ("{0}x{1}: {2}\t".format(x, y, self.worldMap[y][x]))
            retVal += '\n'
        return(retVal)

    def getX(self) -> int:
        return(self.size[0])

    def getY(self) -> int:
        return(self.size[1])
    
    def getSize(self) -> int:
        return(self.size())

    def getPoint(self, x, y) -> Block:
        return(self.worldMap[y][x])

    ## This prints the world
    def getMap(self) -> list:
        return(self.worldMap)

    ## This generates the the world
    def buildWorld(self) -> None:
        for y in range(self.getY()):
            self.worldMap.append([])
            
            for x in range(self.getX()):
                if(randint(1,100) <= 10):
                    self.worldMap[y].append(Tree(x, y))
                self.worldMap[y].append(Block(x, y))

    def interact(self, x, y) -> None:
        return(self.getPoint(x, y).interact())
        


            
if(__name__ == "__main__"):
    myWorld = World(0)
    myWorld.buildWorld()
