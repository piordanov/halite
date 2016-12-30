from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("piordanov v2")

def chooseMove(piece, location):
    # patience, young padawan
    border = False
    for d in CARDINALS:
        neighbor = gameMap.getSite(location, d)
        if neighbor.owner != myID:
            border = True
            if neighbor.strength < piece.strength:
                return Move(location, d)

    if not border and piece.strength < (piece.production * 5):
        return Move(location, random.choice(DIRECTIONS))
    else:
        return Move(location, STILL)

while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            piece = gameMap.getSite(location)
            if piece.owner == myID:
                move = chooseMove(piece, location)
                moves.append(move)
    sendFrame(moves)
