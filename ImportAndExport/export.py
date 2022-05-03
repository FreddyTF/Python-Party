# ! encoding-UTF-8
"""export.py
Export data model to a JSON file

author: inf20026@lehre.dhbw-stuttgart.de
date: 26.04.22
version: 0.0.1
license: MIT
"""

import os, sys
import json

# Make it possible to reference a module in the parent directory
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# Import global datamodel
from DataManager.Datamodel import Person, Spielfeld, Party, Beziehung

Person1 = Person(1, 'Peter', 'Prinzessin', 'P', (1,1), (0,0), ['Test1', 'Test2'], 0)
#convert to JSON string
jsonStr = json.dumps(Person1.__dict__)
print(jsonStr)