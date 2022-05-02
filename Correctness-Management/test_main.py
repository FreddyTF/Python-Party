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
