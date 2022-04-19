# ! encoding-UTF-8
"""Datenmodell
Datenmodell das alle Datenklassen enthält

author: name@email
dat: 19.04.22
version: 0.0.1
license: MIT

"""
class Person():

    def __init__(self, name:str, position:tuple, startposition:tuple, beziehung:list, befindlichkeit = 0) -> None:
        self.name = name
        self.beziehung = beziehung
        self.position = position
        self.startposition = startposition
        self.aktuellebefindlichkeit = befindlichkeit
        self.befindlichkeitüberzeit = [self.aktuellebefindlichkeit]

class Spielfeld():

    def __init__(self, höhe:int, weite:int, abbild:list) -> None:
        self.höhe = höhe
        self.weite = weite
        self.abbild = abbild
        
    def set_abbild(self, position:tuple, wert):
        pass

class Party():
    instance = None
    def __init__(self, spielfeld:Spielfeld, personenliste:list) -> None:
        if self.instance is None:
            self.spielfeld = spielfeld
            self.personenliste = personenliste
            self.gesamtbefindlichkeit = sum([i.aktuellebefindlichkeit for i in self.personenliste])

        return self.instance

    def __init__(self) -> None:
        return self.instance

class Beziehung():
    
    def __init__(self, person:Person, wunschabstand:int, beziehungpositiv:bool) -> None:
        self.person = person
        self.wunschabstand = wunschabstand
        self.beziehungpositiv = beziehungpositiv