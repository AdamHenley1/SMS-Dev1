import random
from random import choice
from WorldGen import *

#global variables
population = 100000

#dictionary
workers = {"fishermen": 30,
           "builders": 40,
           "lumberjack": 10}

#weather is out of 3 --> random.randint(0,3)
weather = {"humidity": 2,
           "precipitation": 1,
           "sunny": 3}



def getPosition(world):
    x = random.randint(0, world.getX())
    y = random.randint(0,world.getY())
    print(x, y)
    print(world.getX(), world.getY())
    print(world.getPoint(595, 694))

andWorld = World(0)
getPosition(andWorld)

people_population = []

def getName():
    name = choice(first) + " " + choice(last)
    return name
    #print(name)    


def getJob():
    fishProb = 1/workers["fishermen"]
    buildProb = 1/workers["builders"]
    lumProb = 1/workers["lumberjack"]
    prob = [fishProb, buildProb, lumProb]
    prob.sort(reverse = True)

    n = random.random()
    #print(n)

    mid = prob[0]-prob[1]
    #print(prob[0], " ", prob[1], " ", mid)
    if prob[0] - n < mid/2:
        where = 0
    else:
        where = 1
    if prob[where] == fishProb:
        workers["fishermen"] = workers["fishermen"] + 1
        return "fishermen"
    elif prob[where] == buildProb:
        workers["builders"] = workers["builders"] + 1
        return "builders"
    else:
        workers["lumberjack"] = workers["lumberjack"] + 1
        return "lumberjack"
    
    #print(workers)

class people:
    def __init__(self, naming, ):
        self.job = getJob()
        self.name = naming
        self.inventory = {"gold":0,
                          "wood": 0,
                          "fish": 0}

    def return_job(self):
        return self.job
    def return_name(self):
        return self.name
    def add_money(self, amount):
        self.inventory["gold"] = self.inventory["gold"] + amount
    def add_wood(self, wood):
        self.inventory["wood"] = self.inventory["wood"] + wood
    def add_fish(self,fish):
        self.inventory["fish"] = self.inventory["fish"] + fish

for i in range(population):
    temp = getName()
    temp = people(temp)
    people_population.append(temp)
#def person(age = 0):
for i in range(population):
    temp = people_population[i]
    print("Name:",temp.return_name(),", Job:",temp.return_job())