""" test_main

    * all basic-tests

    author:     Kania,Tomasz
    date:       02.05.2022
    version:    0.1 demo
    license:    free
"""

import unittest
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


if __name__ == '__main__':
    unittest.main()
