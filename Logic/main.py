# ! encoding-UTF-8
"""
main.py -

author: inf20026@lehre.dhbw-stuttgart.de
date: 26.04.22
version: 0.0.1
license: MIT
"""
import math


def simulation(party):
    party.stillRunning = True
    party.paused = False
    while party.stillRunning:
        calculateIteration(party)
        while party.paused:
            pass


def calculateBestPositionForPerson(person, party):
    fieldsList = getNeighborFields(person, party.spielfeld)
    neuBefindlichkeiten = []
    for field in fieldsList:
        neuBefindlichkeiten.append((calculateWellBeeing(person, field, party), field))
    print(neuBefindlichkeiten)
    maxBefindlichkeit = person.aktuellebefindlichkeit
    newField = person.position
    for befindlichkeit in neuBefindlichkeiten:
        if befindlichkeit[0] > maxBefindlichkeit:
            maxBefindlichkeit = befindlichkeit[0]
            newField = befindlichkeit[1]
    return newField, maxBefindlichkeit


def calculateOnePerson(party, person):
    newField, maxBefindlichkeit = calculateBestPositionForPerson(person, party)
    party.spielfeld.abbild[person.position[0]][person.position[1]] = '#'
    party.spielfeld.abbild[newField[0]][newField[1]] = person.name[0]
    person.position = newField
    person.aktuelleBefindlichkeit = maxBefindlichkeit

def calculateIteration(party):
    for person in party.personenliste:
        calculateOnePerson(party, person)



def getNeighborFields(person, spielfeld):
    fieldslist = []
    position = person.position
    for i in range(-1, 2):
        for j in range(-1, 2):
            newY = position[1] + i
            newX = position[0] + j
            if spielfeld.raum_hoehe > newY >= 0:
                if spielfeld.raum_breite > newX >= 0:
                    if isPositionFree((newX, newY), spielfeld, person):
                        fieldslist.append([newX, newY])
    return fieldslist


def isPositionFree(position, spielfeld, person):
    if spielfeld.abbild[position[0]][position[1]] in ['#', person.name[0]]:
        return True
    return False


def calculateDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def calculateWellBeeing(person, field, party):
    spielfeld = party.spielfeld
    beziehungsbefindlichkeiten = []
    maxDistance = math.sqrt(
            spielfeld.raum_breite ** 2 + spielfeld.raum_hoehe ** 2)

    for beziehung in [i for i in person.beziehung if person.id != i.personid]:
        wunschAbstand = beziehung.wunschabstand
        if beziehung.personid == 0:
            tatAbstand = maxDistance
            for i in range(spielfeld.tisch_hoehe):
                for j in range(spielfeld.tisch_breite):
                    # spielfeld.abbild[spielfeld.tisch_x + j][spielfeld.tisch_y + i]
                    tischField = (spielfeld.tisch_x + j, spielfeld.tisch_y + i)
                    distance = calculateDistance(tischField, field)
                    tatAbstand = distance if distance < tatAbstand else tatAbstand
        else:
            personBeziehung = [i for i in party.personenliste if i.id == beziehung.personid][0]
            tatAbstand = calculateDistance(field, personBeziehung.position)
            #tatAbstandX = abs(field[0] - personBeziehung.position[0])
            #tatAbstandY = abs(field[1] - personBeziehung.position[1])

        #tatAbstand = math.sqrt(tatAbstandX ** 2 + tatAbstandY ** 2)
        befindlichkeitVonBeziehung = mapping_helper(abs(tatAbstand - wunschAbstand), 0, maxDistance, 5, 1)
        beziehungsbefindlichkeiten.append(befindlichkeitVonBeziehung)
    avgBefindlichkeit = sum(beziehungsbefindlichkeiten) / len(beziehungsbefindlichkeiten)
    return avgBefindlichkeit


# Stolen from Internetz
def mapping_helper(value, rangeAmin, rangeAmax, rangeBmin, rangeBmax):
    rangeAspan = rangeAmax - rangeAmin
    rangeBspan = rangeBmax - rangeBmin

    # Convert the math range into a 0-1 range (float)
    valueScaled = float(value - rangeAmin) / float(rangeAspan)

    # Convert the 0-1 range into a value in the right range.
    return rangeBmin + (valueScaled * rangeBspan)
