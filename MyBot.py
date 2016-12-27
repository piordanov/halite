from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("MyPythonBot")

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            piece = gameMap.getSite(location)
            if piece.owner == myID:
                move = None
                if piece.strength == 0:
                    move = Move(location, STILL)
                else:
                    move = Move(location, random.choice(DIRECTIONS))
                moves.append(move)
    sendFrame(moves)
