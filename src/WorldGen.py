## We need a lot of maths for this generation
from math import *
from random import *

global FISH
global WOOD
FISH = Fish(0)
WOOD = Wood(0)


## The items are a collection of (guess what) items that people
## can collect, such as fish, wood, and many more!
class Item:
    def __init__(self, name, count) -> None:
        self.name = name
        self.count = count

    def __add__(self, other) -> int:
        return Item(self.name, self.count + other.count)

    def __str__(self) -> int:
        return("{0} {1}".format(self.count, self.name))

    def getCount(self) -> int:
        return(self.count)

    def gained(self, n) -> None:
        self.count += n


class Wood(Item):
    def __init__(self, count) -> None:
        super().__init__("Wood", count)

class Fish(Item):
    def __init__(self, count) -> None:
        super().__init__("Fish", count)



## The Blocks are the building blocks of the map: everything is made
## out of them.
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

    def interact(self) -> Wood:
        return("td", Wood(randint(5,20)))

## Specific class for water
class Water(Block):
    def __init__(self, x, y) -> None:
        ## f is fishable
        super().__init__(x, y, "Water", False, "f")

    def interact(self) -> Fish:
        caught = randint(1, 5)
        if(caught == 1):
            return(Fish(1))
        return(Fish(0))
        

            
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

    def setPoint(self, block, x, y):
        self.worldMap[y][x] = block

    ## Checks what specific instruction codes mean,
    ## and executes them.
    def instCode(self, code, x, y) -> None:
        if(code == "td"):
            self.setPoint(Block(x, y), x, y)

    ## This generates the the world
    def buildWorld(self) -> None:
        for y in range(self.getY()):
            self.worldMap.append([])
            
            for x in range(self.getX()):
                if(randint(1,100) <= 10):
                    self.worldMap[y].append(Tree(x, y))
                self.worldMap[y].append(Block(x, y))

    def interact(self, x, y) -> None:
        inter = self.getPoint(x, y).interact()
        print(type(inter), inter)
        if(type(inter) != type((0, 1))):
            return(inter)
        
        self.instCode(inter[0], x, y)
        return(inter[1])
        

            
if(__name__ == "__main__"):
    myWorld = World(0)
    myWorld.buildWorld()
    print(myWorld)
