import random
from random import choice

#global variables
population = 100

#dictionary
workers = {"fishermen": 30,
           "builders": 40,
           "lumberjack": 10}

#weather is out of 3 --> random.randint(0,3)
weather = {"humidity": 2,
           "precipitation": 1,
           "sunny": 3}

people_population = []

def getName():
    first = ["Adam", "Andrea", "Cameron"]
    last = ["Henley", "Crossa", "Ayres"]
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
    def __init__(self, naming):
        self.job = getJob()
        self.name = naming
    def return_job(self):
        return self.job
    def return_name(self):
        return self.name

for i in range(population):
    temp = getName()
    temp = people(temp)
    people_population.append(temp)
#def person(age = 0):
for i in range(population):
    temp = people_population[i]
    print("Name:",temp.return_name(),", Job:",temp.return_job())