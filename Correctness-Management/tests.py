""" test_main

    * all basic-tests are implemented here
    * 1st Test if the files do exist
    * 2nd Test Basic test of functionality
    * 3rd Test False Test Statements

    author:     inf20086@lehre.dhbw-stuttgart.de
    date:       11.05.2022
    version:    0.0.1
    license:    MIT
"""

import unittest
from pathlib import Path

from ImportAndExport.importData import importFromJson
from DataManager.Datamodel import Party, Spielfeld
import main


# All tests are written in this file
# -> different classes can be used thou


# TestOfExistence tests if the Programm files do exist
# if not then tests are failed
class TestOfExistence(unittest.TestCase):
    def test_gui_exist(self):
        path1 = Path('../VisualisationAndStatistics/gui.py')
        assert path1.is_file()

    def test_logic_exist(self):
        path2 = Path('../Logic/main.py')
        assert path2.is_file()

    def test_import_export_exist(self):
        path3 = Path('../ImportAndExport/importData.py')
        path4 = Path('../ImportAndExport/exportData.py')
        assert path3.is_file()
        assert path4.is_file()

    def test_datamanager_exist(self):
        path5 = Path('../DataManager/Datamodel.py')
        path6 = Path('../DataManager/__init__.py')
        assert path5.is_file()
        assert path6.is_file()


class TestCase(unittest.TestCase):

    # 1.st import file
    # 2. check for equal in specified function
    # 3. run TEst
    def test_main_true(self):
        self.assertEqual(main.test1(), "Hello Python")

    def test_import_true_1(self):
        # Testparty = Party()
        # self.assertEqual(importFromJson("../config_example.json"), Testparty)

        self.assertIsInstance(importFromJson("../config_example.json"), Party)

    def test_import_true_2(self):
        # Testparty = Party().
        # self.assertEqual(importFromJson("../config_example.json"), Testparty)

        self.assertIsInstance(importFromJson("../config_example_2.json"), Party)

    def test_import_true_3(self):
        # Testparty = Party().
        # self.assertEqual(importFromJson("../config_example.json"), Testparty)

        self.assertIsInstance(importFromJson("../config_example_3.json"), Party)

    def test_import_true_4(self):
        # Testparty = Party().
        # self.assertEqual(importFromJson("../config_example.json"), Testparty)

        self.assertIsInstance(importFromJson("../config_example_4.json"), Party)


class FalseTestCase(unittest.TestCase):

    def test_main_false(self):
        self.assertNotEqual(main.test1(), "This Test should fail")





if __name__ == '__main__':
    unittest.main()
