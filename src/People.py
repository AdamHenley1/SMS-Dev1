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
    validator = False
    while False:
        x = randint(0, world.getX())
        y = randint(0,world.getY())
        checker = world.getPoint(x, y)
        if checker == " Dirt":
            temp = people(getName())
            people_population.append(temp)
            world.setPoint(person,x,y)
            validator = True
        else: pass



## Chooses a new name from 487861706 different possibilities
def getName():
    fNames = 5494
    sNames = 88799
    FName_Choise = randint(1,fNames)
    SNames_Choise = randint(1,sNames)
    ffile = open('FirstNames.txt') 
    fcontent = ffile.readlines() 
    file = open('LastNames.txt') 
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
    def __init__(self, naming, x, y):
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
        for y in range(radius):
            for x in range(radius):
                print(x, y)
            

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
        



        
## This will run if the file is directly called,
## but not if it is imported as a library.
if(__name__ == "__main__"):
    andWorld = World(0)
    andWorld.buildWorld()
    spawn(andWorld)
    
    for i in range(population):
        temp = people(getName())
        people_population.append(temp)
        #def person(age = 0):
    for i in range(population):
        temp = people_population[i]
        print("Name:",temp.return_name(),", Job:",temp.return_job())            
