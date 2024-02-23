from random import *
from WorldGen import *

#global variables
population = 100000

#dictionary
workers = {"fishermen": 30,
           "builders": 40,
           "lumberjack": 10}

#weather is out of 3 --> randint(0,3)
weather = {"humidity": 2,
           "precipitation": 1,
           "sunny": 3}

people_population = []


def spawn(world):
    x = randint(0, world.getX())
    y = randint(0,world.getY())
    print(world.getPoint(x, y))
    """while world.getPoint(x, y) != " ":
        x = randint(0, world.getX())
        y = randint(0,world.getY())
    temp = people(getName())
    people_population.append(temp)"""
    



## Chooses a new name from 487861706 different possibilities
def getName():
    fNames = []
    sNames = []

    with open("assets/FirstNames.txt") as fNamesFile:
        for fName in fNamesFile:
            fNames.append(fName[:-1])
    with open("assets/LastNames.txt") as sNamesFile:
        for sName in sNamesFile:
            sNames.append(sName[:-1])

    
    name = choice(fNames).title() + " " + choice(sNames).title()
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

class people:
    def __init__(self, naming):
        self.job = getJob()
        self.name = naming
        self.inventory = {"Money":0,
                          "Wood": 0,
                          "fish": 0}

    def add_money(self, amount):
        self.inventory["Money"] += amount
    def add_wood(self, wood):
        self.inventory["Wood"] += wood
    def add_fish(self,fish):
        self.inventory["Fish"] += fish


    def return_job(self):
        return self.job
    def return_name(self):
        return self.name
    def return_money(self):
        return self.inventory("Money")
    def add_money(self, amount):
        self.inventory["gold"] = self.inventory["gold"] + amount
    def add_wood(self, wood):
        self.inventory["wood"] = self.inventory["wood"] + wood
    def add_fish(self,fish):
        self.inventory["fish"] = self.inventory["fish"] + fish

        
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
            
