""" test_main

    * all basic-tests

    author:     Kania,Tomasz
    date:       02.05.2022
    version:    0.1 demo
    license:    free
"""

import unittest

from ImportAndExport.importData import importFromJson
from DataManager.Datamodel import Party, Spielfeld, Person, Beziehung
import main


# All tests are written in this file
# -> different classes can be used thou


class TestCase(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # 1.st import file
    # 2. check for equal in specified function
    # 3. run TEst
    def test_main(self):
        self.assertEqual(main.test1(), "Hello Python")

    def test_import(self):
        Testparty = Party(
            Spielfeld(9, 14, abbild=[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', 'T', 'T', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', 'T', 'T', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', 'T', 'T', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]),
            [Person(1, 'Brigitte', [5.75, 5.75], [5.75, 5.75], Beziehung(1, 0), 0),
             Person(2, 'Caesar', [7.25, 6.75], [7.25, 6.75], Beziehung(1, 0), 0)])

        # self.assertEqual(importFromJson("../config_example.json"), Testparty)

        self.assertIsInstance(importFromJson("../config_example.json"), Party)

    def test_(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
