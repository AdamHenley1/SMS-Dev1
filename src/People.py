import random
from random import choice
class Person:
    def __init__(self, inventory, age = 0):
        self.age = age
        self.inventory = inventory

def getName():
    first = ["Adam", "Andrea", "Cameron"]
    last = ["Henley", "Crossa", "Ayres"]
    name = choice(first) + " " + choice(last)
    print(name)    
getName()

workers = {"fishermen": 30,
           "builders": 40,
           "lumberjack": 10}

#weather is out of 3 --> random.randint(0,3)
weather = {"humidity": 2,
           "precipitation": 1,
           "sunny": 3}

population = 100

def getJob():
    fishProb = 1/workers["fishermen"]
    buildProb = 1/workers["builders"]
    lumProb = 1/workers["lumberjack"]
    prob = [fishProb, buildProb, lumProb]
    prob.sort(reverse = True)

    n = random.random()
    print(n)

    mid = prob[0]-prob[1]
    print(prob[0], " ", prob[1], " ", mid)
    if prob[0] - n < mid/2:
        where = 0
    else:
        where = 1
    if prob[where] == fishProb:
        workers["fishermen"] = workers["fishermen"] + 1
    elif prob[where] == buildProb:
        workers["builders"] = workers["builders"] + 1
    else:
        workers["lumberjack"] = workers["lumberjack"] + 1

    print(workers)
getJob()
    
    

#def person(age = 0):
