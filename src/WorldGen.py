from random import randint


## The items are a collection of (guess what) items that people
## can collect, such as fish, wood, and many more!
class Item:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __add__(self, other):
        return Item(self.name, self.count + other.count)

    def __str__(self):
        return("{0} {1}".format(self.count, self.name))

    def getCount(self):
        return(self.count)

    def gained(self, n):
        self.count += n


class Wood(Item):
    def __init__(self, count):
        super().__init__("Wood", count)

class Fish(Item):
    def __init__(self, count):
        super().__init__("Fish", count)



## The Blocks are the building blocks of the map: everything is made
## out of them.
## s is shovel, p is pickaxe
## The first character of the name decides what it
## will be called on the map.
class Block:
    def __init__(self, x, y, name = " dirt", move = True, info = "ms"):
        self.name = name
        self.move = move
        self.info = info
        self.x = x
        self.y = y

    def __str__(self):
        return(self.name)

    def getName(self):
        return(self.name[0])

    def setBlock(self, name, move, info):
        self.name = name
        self.move = move
        self.info = info

    def setStone(self):
        self.setBlock("Stone", True, "mp")

    def setWWall(self):
        self.setBlock("W-Wall", False, "ma")

    def setTree(self):
        self.setBlock("Tree", False, "ma")

    def getProperties(self):
        return(0)

    def interact(self):
        return(None)

    
## Specific class for trees.
class Tree(Block):
    def __init__(self, x, y):
        super().__init__(x, y, "Tree", False, "ma")

    def interact(self):
        return("td", Wood(randint(5,20)))

## Specific class for water
class Water(Block):
    def __init__(self, x, y):
        ## f is fishable
        super().__init__(x, y, "Water", False, "f")

    def interact(self):
        caught = randint(1, 5)
        if(caught == 1):
            return(Fish(1))
        return(Fish(0))
        

            
## A class for the world.
## This goes y/x, not x/y as everything else
## in the known universe does.
class World:
    def __init__(self, name, sizeX = 1024, sizeY = 1024):
        self.ID = name
        self.size = (sizeX, sizeY)
        self.worldMap = []

    def __str__(self):
        retVal = ""
        for y in range(self.getY()):
            for x in range(self.getX()):
                #retVal += ("{0}x{1}: {2}\t".format(x, y, self.worldMap[y][x]))
                retVal += self.getPointName(x, y)
            retVal += '\n'
        return(retVal)

    def getX(self):
        return(self.size[0])

    def getY(self):
        return(self.size[1])
    
    def getSize(self):
        return(self.size())

    def getPoint(self, x, y):
        return(self.worldMap[y][x])

    def getPointName(self, x, y):
        return(self.getPoint(x, y).getName())

    ## This prints the world
    def getMap(self):
        return(self.worldMap)

    def setPoint(self, block, x, y):
        self.worldMap[y][x] = block

    ## Checks what specific instruction codes mean,
    ## and executes them.
    def instCode(self, code, x, y):
        if(code == "td"):
            self.setPoint(Block(x, y), x, y)

    ## Identifies a block given its ID and x/y coordinates.
    def identify(self, block, x, y):
        if(block == 'W'):
            return(Water(x, y))
        elif(block == 'T'):
            return(Tree(x, y))
        else:
            return(Block(x, y))

    ## Find where water should be put, and puts it
    ## there.
    def createWater(self):
        area = self.getX() * self.getY()
        point = randint(1, area)

        waterX = point % self.getY()
        waterY = point // self.getY()

        watersY = int(self.getY() * 0.1)

        ## What the height of the river should be.
        for y in range(int(waterY - (self.getY() * 0.1)), int(waterY + (self.getY() * 0.1))):
            ## What the length of the river should be.
            for x in range(randint(int(-1 * self.getX()), 0), randint(1, int(self.getX() * 0.1))):
                watersX = waterX + x

                ## Catch if the river is too far to the right, and wraps it around if it is.
                if(watersX > self.getX()):
                    watersX -= self.getX()
                    
                self.setPoint(Water(watersX, y), watersX, y)

        
    ## This generates the the world.
    def buildWorld(self):
        for y in range(self.getY()):
            self.worldMap.append([])
            
            for x in range(self.getX()):
                if(randint(1,100) <= 20):
                    self.worldMap[y].append(Tree(x, y))
                self.worldMap[y].append(Block(x, y))

        ## Makes sure that there's water.
        watered = False
        while(not(watered)):
            try:
                self.createWater()
                watered = True
            except:
                continue

    ## Just writes to a specified file instead of stdout.
    def saveWorld(self, saveFile):
        saveData = ""
        for rows in self.worldMap:
            for point in rows:
                saveData += point.getName()
            saveData += '\n'
            
        with open(saveFile, 'w') as save:
            save.write(saveData)

    ## Lets a user load a world from a file.
    def loadWorld(self, saveFile):
        x = 0
        y = 0
        with open(saveFile, 'r') as data:
            for rows in data:
                x = 0
                self.worldMap.append([])
                for block in rows:
                    self.worldMap[-1].append(self.identify(block, x, y))
                    x += 1
                y += 1

    ## Interact with a given point on the map
    def interact(self, x, y):
        inter = self.getPoint(x, y).interact()
        if(type(inter) != type((0, 1))):
            return(inter)
        
        self.instCode(inter[0], x, y)
        return(inter[1])
        

            
if(__name__ == "__main__"):
    print()
    myWorld = World(0, sizeX = 64, sizeY = 32)
    #myWorld.buildWorld()

    myWorld.loadWorld("saveData")
    print(myWorld)
    #myWorld.loadWorld("saveData")
    #print(myWorld)
