def simulation(party):
    party.stillRunning = True
    party.paused = False
    while party.stillRunning:
        calculateIteration(party)
        while party.paused:
            pass
        

def calculateIteration(party):
    for person in party.personList:
        fieldsList = getNeighborFields(person.position, party.spielfeld)
        neuBefindlichkeiten = []
        for field in fieldsList:
            neuBefindlichkeiten.append(calculateWellBeeing(person, field))
        


def getNeighborFields(position, spielfeld):
    fieldslist = []
    for i in range (-1, 1):
        for j in range (-1, 1):
            newY = position[1]+i
            newX = position[0]+j
            if newY  < spielfeld.height and newY >= 0:
                if newX < spielfeld.width and newX >= 0:
                    if isPositionFree((newX,newY),spielfeld):
                        fieldslist.append([newX, newY])
    return fieldslist

def isPositionFree(position,spielfeld):
    if spielfeld [position[0],position[1]] == '':
        return True
    return False

def calculateWellBeeing(person, field):
    aktuelleBefindlichkeit = person.aktuelleBefindlichkeit
    beziehungen = []
    for beziehung in person.beziehung:
        wunschAbstand = beziehung.wunschabstand
        tatAbstandX = Math.abs(field[0] - beziehung.person.position[0])
        tatAbstandY = Math.abs(field[1] - beziehung.person.position[1])
        tatAbstand = Math.sqrt(tatAbstandX * tatAbstandX + tatAbstandY * tatAbstandY)
        befindlichkeitVonBeziehung = Math.map(tatAbstand - wunschAbstand