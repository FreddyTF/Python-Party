""" test_main

    * main test-starter

    author:     Kania,Tomasz
    date:       02.05.2022
    version:    0.1 demo
    license:    free
"""

import sys
import unittest
import tests

### DO NOT DELETE THIS FILE
### All tests are going to start from this file and logging is also implemented here

def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(tests)
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('output.txt', 'w') as f:
        main(f)
