# ! encoding-UTF-8
"""export.py
Export data model to a JSON file

author: inf20026@lehre.dhbw-stuttgart.de
date: 26.04.22
version: 0.0.1
license: MIT
"""

import json
import sys, os

# Make it possible to reference a module in the parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataManager.Datamodel import Person, Party, Spielfeld, Beziehung

def importFromJson(configPath):

    with open("../config_example.json", 'r') as f:
        data = json.load(f)
    
    # Create personlist
    personlist = []
    for person in data["Personen"]:
        position = person["startposition"][0], person["startposition"][1]
        tmp = Person(person["id"], person["name"], position, position, None)
        personlist.append(tmp)

    # Add relations
    for count, person in enumerate(personlist):
        relationlist = []
        for relation in data["Wunschabstaende"]:
            if person.id == relation["person1_id"]:
                tmp = Beziehung(relation["person2_id"], relation["wunschabstand"])
                relationlist.append(tmp)
        person.beziehung = relationlist
        personlist[count] = person
    
    # Add spielfeld
    ylist = []
    for y in range(data["Spielfeld"]["raum_breite"]):
        xlist = []
        for x in range(data["Spielfeld"]["raum_hoehe"]):
            if data["Spielfeld"]["tisch_y"] <= x <= (data["Spielfeld"]["tisch_y"]+data["Spielfeld"]["tisch_hoehe"]-1) \
                    and data["Spielfeld"]["tisch_x"] <= y <= (data["Spielfeld"]["tisch_x"]+data["Spielfeld"]["tisch_breite"]-1):
                tmp = "T"
            else:
                tmp = "#"
            xlist.append(tmp)
        ylist.append(xlist)

    # Add persons to spielfeld
    for person in personlist:
        ylist[person.startposition[0]][person.startposition[1]] = person.name[0]

    spielfeld = Spielfeld(data["Spielfeld"]["raum_hoehe"], data["Spielfeld"]["raum_breite"],
                          data["Spielfeld"]["tisch_breite"], data["Spielfeld"]["tisch_hoehe"],
                          data["Spielfeld"]["tisch_x"], data["Spielfeld"]["tisch_y"],
                          data["Spielfeld"]["Iterationen"], ylist)

    # Create Party
    party = Party(spielfeld, personlist)
    return party

party = importFromJson("config_example.json")
print(party.spielfeld.abbild)