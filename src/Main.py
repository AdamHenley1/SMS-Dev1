from WorldGen import *
from People import *


if(__name__ == "__main__"):
    theWorld = World(0, sizeX = 200, sizeY = 64)
    theWorld.buildWorld()
    print(theWorld)
