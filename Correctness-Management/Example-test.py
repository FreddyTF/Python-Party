import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

#1.st import file
#2. check for equal in specified function
#3. run TEst
    def test_main(self):
        self.assertEqual(main.test1(),"Hello Python")

if __name__ == '__main__':
    unittest.main()