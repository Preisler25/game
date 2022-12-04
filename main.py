#region Import
import random
#endregion
#region Spawn
#gen map (4x4 dict with value 0) format (x,y):value
def genGameMap():
    tempMap = dict()
    for y in range(4):
        for x in range(4):
            tempMap[(x,y)] = 0
    return tempMap

#start game gen 2 random numbers
def start(Map):
    Map = genRandom(Map)
    Map = genRandom(Map)
    return Map
#endregion
#region Game
def getInputs():
    temp = input("")
    return temp

def wantToPlay(Map, temp):
    if temp == "0":
        return False
    else:
        return True

def keydown(event, Map):
    match event:
        case "w":
            return moveUp(Map)
        case "a":
            return moveLeft(Map)
        case "s":
            return moveDown(Map)
        case "d":
            return moveRight(Map)
        case other:
            print("")
#endregion
#region Movement
def moveUp(Map):
    for x in range(3, -1, -1):
        for y in range(3, 0, -1):
            if Map[(x,y)] != 0:
                if Map[(x,y-1)] == 0:
                    Map[(x,y-1)] = Map[(x,y)]
                    Map[(x,y)] = 0
                elif Map[(x,y-1)] == Map[(x,y)]:
                    Map[(x,y-1)] += Map[(x,y)]
                    Map[(x,y)] = 0
                else:
                    continue
    return Map

def moveLeft(Map):
    for y in range(3, -1, -1):
        for x in range(3, 0, -1):
            if Map[(x,y)] != 0:
                if Map[(x-1,y)] == 0:
                    Map[(x-1,y)] = Map[(x,y)]
                    Map[(x,y)] = 0
                elif Map[(x-1,y)] == Map[(x,y)]:
                    Map[(x-1,y)] += Map[(x,y)]
                    Map[(x,y)] = 0
                else:
                    continue
    return Map

def moveDown(Map):
    for x in range(3, -1, -1):
        for y in range(3):
            if Map[(x,y)] != 0:
                if Map[(x,y+1)] == 0:
                    Map[(x,y+1)] = Map[(x,y)]
                    Map[(x,y)] = 0
                elif Map[(x,y+1)] == Map[(x,y)]:
                    Map[(x,y+1)] += Map[(x,y)]
                    Map[(x,y)] = 0
                else:
                    continue
    return Map

def moveRight(Map):
    for y in range(4):
        for x in range(3):
            if Map[(x,y)] != 0:
                if Map[(x+1,y)] == 0:
                    Map[(x+1,y)] = Map[(x,y)]
                    Map[(x,y)] = 0
                elif Map[(x+1,y)] == Map[(x,y)]:
                    Map[(x+1,y)] += Map[(x,y)]
                    Map[(x,y)] = 0
                else:
                    continue
    return Map
#endregion    
#region Randomgen
#gen random number (0 - 3) and if it is free gets a value of 2 if not retrys
def genRandom(Map):
    while True:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if testIfNull((x,y), Map):
            Map[(x,y)] = 2
            return Map

#test if the position is free
def testIfNull(temp, Map):
    if Map[temp] == 0:
        return True
    else:
        return False
#endregion
#region Test if Over
def testIfOver(Map):
    if 0 not in Map.values():
        return True
#endregion
#region Main
def main():
    ingame = True
    gameMap = genGameMap()
    gameMap = start(gameMap)
    while ingame:
        user_input = getInputs()
        ingame = wantToPlay(gameMap, user_input)
        if ingame == False:
            break
        gameMap = keydown(user_input, gameMap)
        gameMap = genRandom(gameMap)
        if testIfOver(gameMap):
            print("Game Over")
            break
        print(f"{gameMap[0,0]} {gameMap[1,0]} {gameMap[2,0]} {gameMap[3,0]}\n{gameMap[0,1]} {gameMap[1,1]} {gameMap[2,1]} {gameMap[3,1]}\n{gameMap[0,2]} {gameMap[1,2]} {gameMap[2,2]} {gameMap[3,2]}\n{gameMap[0,3]} {gameMap[1,3]} {gameMap[2,3]} {gameMap[3,3]}")
main()
#endregion