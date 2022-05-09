# ! encoding-UTF-8
"""Datenmodell
Datenmodell das alle Datenklassen enthält

author: inf20079@lehre.dhbw-stuttgart.de
dat: 19.04.22
version: 0.0.1
license: MIT

"""
class Person():

    def __init__(self, id:int, name:str, position:tuple, startposition:tuple, beziehung:list, befindlichkeit = 0) -> None:
        self.id = id
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
        """Überschreibt abbild an Position x,y 

        Args:
            position (tuple): X- und Y-Koordinate
            wert (_type_): Neuer Wert

        Returns:
            _type_: Neuer Wert
        """
        self.abbild[position[0]][position[1]] = wert
        return wert

class Party():

    instance = None

    def __init__(self) -> None:
        return self.instance
    
    def __init__(self, spielfeld:Spielfeld, personenliste:list) -> None:
        if self.instance is None:
            self.spielfeld = spielfeld
            self.personenliste = personenliste
            self.gesamtbefindlichkeit = sum([i.aktuellebefindlichkeit for i in self.personenliste])

        return self.instance

    

class Beziehung():
    
    def __init__(self, personid:int, wunschabstand:int) -> None:
        self.personid = personid
        self.wunschabstand = wunschabstand