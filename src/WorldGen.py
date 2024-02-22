## We need a lot of maths for this generation
from math import *
from random import *


## List of block types.
## Each tuple is block: name, movable, destroy with
## s is shovel, p is pickaxe
class Block:
    def __init__(self, name = "Dirt", move = True, info = "ms"):
        self.name = name
        self.move = move
        self.info = info

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

    def getProperties

def Tree(Block):
    def __init__(self, name = "Tree", move = False, info = "ma")

        
## A class for the world
class World:
    def __init__(self, name, sizeX = 4, sizeY = 4) -> None:
        self.ID = name
        self.size = (sizeX, sizeY)
        self.worldMap = []

    def __str__(self) -> str:
        return("No")

    def getX(self) -> int:
        return(self.size[0])

    def getY(self) -> int:
        return(self.size[1])
    
    def getSize(self) -> int:
        return(self.size())

    def buildWorld(self) -> None:
        for y in range(self.getY()):
            self.worldMap.append([])
            
            for x in range(self.getX()):
                self.worldMap[y].append(Block())
                
    def getWorld(self) -> None:
        for y in range(self.getY()):
            for x in range(self.getX()):
                print("{0}x{1}: {2}\t".format(x, y, self.worldMap[y][x]), end = '')
            print()



world = World(0, sizeY = 10)
world.buildWorld()
world.getWorld()
