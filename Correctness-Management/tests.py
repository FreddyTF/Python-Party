import unittest
import main

# All tests are written in this file
#-> different classes can be used thou


class TestCase(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

#1.st import file
#2. check for equal in specified function
#3. run TEst
    def test_main(self):
        self.assertEqual(main.test1(),"Hello Python")
        print("Hello World")

if __name__ == '__main__':
    unittest.main()