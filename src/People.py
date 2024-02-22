import random
from random import choice
#class Person:
#    def __init__(self, age = 0):
#        self.age = age

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

    highest = max(prob)



    n = random.random()
    print(n)

    mid = prob[0]-prob[1]
    #if prob[0] - n < mid/2
        


getJob()
    
    

#def person(age = 0):
