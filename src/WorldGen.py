## We need a lot of maths for this generation
from math import *
from random import *


## List of block types.
## Each tuple is block: name, movable, destroy with
## s is shovel, p is pickaxe
nBlock = lambda n, m, i : {"name": n, "move": m, "info": i}
BLOCKS = [nBlock("Dirt", True, "ms"), nBlock("Wall", False, "mp"), nBlock("W-Floor", True, "ma"), nBlock("Water", False, "fr")]
class Block:
    def __init__(self, name = "Dirt", move = True, info = "ms"):
        self.name = name
        self.move = move
        self.info = info

    def newBlock(self):
        return(0)

        
## A class for the world
class World:
    def __init__(self, name, sizeX = 4, sizeY = 4):
        self.ID = name
        self.size = (sizeX, sizeY)
        self.worldMap = list()

    def __str__(self):
        return("No")
    
    def getSize(self):
        return(self.size)

    def getWorld(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                print("{0}x{1} ".format(x, y), end = '')
            print()

    def buildWorld(self):
        for y in range(self.size[1]):
            for x in raneg(self.size[0]):
                self.worldMap[x][y] = 

world = World(0, sizeY = 10)
#world.getWorld()
