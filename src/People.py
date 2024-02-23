from random import *
from WorldGen import *

#global variables
population = 100

#dictionary
workers = {"fishermen": 30,
           "builders": 40,
           "lumberjack": 10}

#weather is out of 3 --> randint(0,3)
weather = {"humidity": 2,
           "precipitation": 1,
           "sunny": 3}

people_population = []

#chooses a random point in the map and checks if it's a space, if so then spawns
def spawn(world):
    placed = False
    while(placed != True):
        pointX = randint(0, world.getX())
        pointY = randint(0, world.getY())

        try:
            if(world.getPoint(pointX, pointY).getName() == ' '):
                world.setPoint(NPC(pointX, pointY, "Gary"), pointX, pointY)
                placed = True
                
        except:
            continue



## Chooses a new name from 487861706 different possibilities
def getName():
    fNames = 5494
    sNames = 88799
    FName_Choise = randint(1,fNames)
    SNames_Choise = randint(1,sNames)
    ffile = open('SMS-Dev1/src/FirstNames.txt') 
    fcontent = ffile.readlines() 
    file = open('SMS-Dev1/src/LastNames.txt') 
    scontent = file.readlines() 
    name = choice(fcontent[FName_Choise:FName_Choise+1]) + choice(scontent[SNames_Choise:SNames_Choise+1])
    return name


def getJob():
    fishProb = 1/workers["fishermen"]
    buildProb = 1/workers["builders"]
    lumProb = 1/workers["lumberjack"]
    prob = [fishProb, buildProb, lumProb]
    prob.sort(reverse = True)

    n = random()
    #print(n)

    mid = prob[0]-prob[1]
    #print(prob[0], " ", prob[1], " ", mid)
    if prob[0] - n < mid/2:
        where = 0
    else:
        where = 1
    if prob[where] == fishProb:
        workers["fishermen"] += 1
        return "fishermen"
    elif prob[where] == buildProb:
        workers["builders"] += 1
        return "builders"
    else:
        workers["lumberjack"] += 1
        return "lumberjack"
    
    #print(workers)

class People:
    def __init__(self, naming, x = 0, y = 0):
        self.job = getJob()
        self.name = naming
        self.__pos = [x, y]
        self.inventory = {"Money":0,
                          "Wood": 0,
                          "Fish": 0}


    def getJob(self):
        return self.job
    
    def getName(self):
        return self.name
    
    def getMoney(self):
        return self.inventory("Money")

    def getFish(self):
        return self.inventory["Fish"]

    def getWood(self):
        return self.inventory["Wood"]
    
    def addMoney(self, amount):
        self.inventory["Money"] += amount
        
    def addWood(self, wood):
        self.inventory["Wood"] += wood
        
    def addFish(self,fish):
        self.inventory["Fish"] += fish

    ## Moves the NPC.
    def move(self, x, y):
        self.__pos[0] += x
        self.__pos[1] += y

    ## Scans the local area for a specific block.
    def scanFor(self, block, radius):
        #        for y in range(radius):
        #            for x in range(radius):
        #                print(x, y)
        return(None)
            

    ## Finds some fish.
    def findFish(self):
        if(randint(0, 1) == 0):
            self.move(0, 1)
        else:
            self.move(1, 0)

    ## Finds some wood.
    def findWood(self):
        return(None)

        
    ## Wanting something prefixes the variable with a 'w'.
    def needs(self):
        wFish = getFish()
        wWood = getWood()

        if(wFish < 2):
            self.findFish(self)
            
        elif(radint(0, 10) < 6):
            self.findWood(self)
        

def startMenu():

    
    print("Welcome to HAC society!")
    newW = input("Would you like to load a saved world? [y / N] ")
    newWorld = World(0)
    
    if(newW.lower() == 'y'):
        saveFile = input("What is the path to the save file: ")
        
        try:
            newWorld.loadWorld(saveFile)
            print("Success!")
            print("Starting world...")
            return(newWorld)
        except:
            print("ERROR: File could not be found. Exiting...")

    else:
        print("Generating a new world...")
        newWorld.buildWorld()
        print("Success!")

        people = input("How many people do you want: ")
        
        x,y = input("How big do you want the world to be [x y]: ").split(" ")
        newWorld = World(0, sizeX = int(x), sizeY = int(y))
        
        print("Spawning people...")
        for i in range(int(people)):
            spawn(newWorld)
        
        print("Starting world...")
        return(newWorld)


        
## This will run if the file is directly called,
## but not if it is imported as a library.
if(__name__ == "__main__"):
    peopleNum = input("How many people do you want: ")
    print("World is 64x16.")
    andWorld = World(0, sizeX = 64, sizeY = 16)
    andWorld.buildWorld()
    for i in range(int(peopleNum)):
        spawn(andWorld)
    print(andWorld)
    
#    for i in range(population):
#        temp = People(getName())
#        people_population.append(temp)
#        #def person(age = 0):
#    for i in range(population):
#        temp = People_population[i]
#        print("Name:",temp.return_name(),", Job:",temp.return_job())            
#
