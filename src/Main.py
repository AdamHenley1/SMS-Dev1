from WorldGen import *
from People import *


if(__name__ == "__main__"):
    theWorld = World(0, sizeX = 12, sizeY = 16)
    theWorld.buildWorld()
    print(theWorld)
