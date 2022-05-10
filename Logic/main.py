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


def calculateIteration(party):
    for person in party.personenliste:
        fieldsList = getNeighborFields(person.position, party.spielfeld)
        neuBefindlichkeiten = []
        for field in fieldsList:
            neuBefindlichkeiten.append((calculateWellBeeing(person, field, party.spielfeld, party), field))
        max = person.aktuellebefindlichkeit
        newField = person.position;
        for befindlichkeit in neuBefindlichkeiten:
            if befindlichkeit[0] > max:
                max = befindlichkeit[0]
                newField = befindlichkeit[1]
        party.spielfeld.abbild[person.position[0]][person.position[1]] = '#'
        party.spielfeld.abbild[field[0]][field[1]] = person.name[0]
        moveTo(person, max, newField)


def moveTo(person, befindlichkeit, field):
    if not (person.position[0] == field[0] and person.position[1] == field[1]):
        person.position = field
        person.aktuelleBefindlichkeit = befindlichkeit


def getNeighborFields(position, spielfeld):
    fieldslist = []
    for i in range(-1, 1):
        for j in range(-1, 1):
            newY = position[1] + i
            newX = position[0] + j
            if newY < spielfeld.raum_hoehe and newY >= 0:
                if newX < spielfeld.raum_breite and newX >= 0:
                    if isPositionFree((newX, newY), spielfeld):
                        fieldslist.append([newX, newY])
    return fieldslist


def isPositionFree(position, spielfeld):
    if spielfeld.abbild[position[0]][position[1]] == '#':
        return True
    return False


def calculateWellBeeing(person, field, spielfeld, party):
    aktuelleBefindlichkeit = person.aktuellebefindlichkeit
    beziehungsbefindlichkeiten = []
    for beziehung in person.beziehung:
        if beziehung.personid == 0:
            continue

        wunschAbstand = beziehung.wunschabstand

        personBeziehung = [i for i in party.personenliste if i.id == beziehung.personid][0]

        tatAbstandX = abs(field[0] - personBeziehung.position[0])
        tatAbstandY = abs(field[1] - personBeziehung.position[1])
        tatAbstand = math.sqrt(tatAbstandX * tatAbstandX + tatAbstandY * tatAbstandY)
        befindlichkeitVonBeziehung = mapping_helper(abs(tatAbstand - wunschAbstand), 0, math.sqrt(
            spielfeld.raum_breite * spielfeld.raum_breite + spielfeld.raum_hoehe * spielfeld.raum_hoehe), 5, 1)
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
