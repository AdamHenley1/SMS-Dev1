from WorldGen import *
from People import *


def startMenu():
    print("Welcome to HAC society!")
    newW = input("Would you like to load a saved world? [y / N] ")

    if(newW.lower() == 'y'):
        newWorld = World(0)
        saveFile = input("What is the path to the save file: ")
        
        try:
            newWorld.loadWorld(saveFile)
            print("Success!")
            print("Starting world...")
            return(newWorld)
        except:
            raise Exception("File could not be found. Exiting...")

    else:
        x,y = input("How big do you want the world to be [x y]: ").split(" ")
        newWorld = World(0, sizeX = int(x), sizeY = int(y))
        print("Generating a new world...")

        newWorld.buildWorld()
        print("Success!")

        people = input("How many people do you want: ")
        
        print("Spawning people...")
        for i in range(int(people)):
            spawn(newWorld)
        
        print("Starting world...")
        return(newWorld)


if(__name__ == "__main__"):
    world = startMenu()
    print(world)
