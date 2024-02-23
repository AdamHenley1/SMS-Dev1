from WorldGen import *
from People import *


def startMenu():
    newWorld = World(0, sizeX = 200, sizeY = 64)
    
    print("Welcome to HAC society!")
    newW = input("Would you like to load a saved world? [y / N] ")
    
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
        
        print("Starting world...")
        return(newWorld)


if(__name__ == "__main__"):
    world = startMenu()
    print(world)
