""" test_main

    * main test-starter
    * all tests are started from here
    * the main-function writes all data to an output-file

    author:     inf20086@lehre.dhbw-stuttgart.de
    date:       11.05.2022
    version:    0.0.1
    license:    MIT
"""

import sys
import unittest
import tests
from datetime import date

# DO NOT DELETE THIS FILE
# All tests are going to start from this file and logging is also implemented here

def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(tests)
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    today = date.today()
    with open('output.txt', 'w') as f:
        f.write(f"This is the output file of the Python-Party Project\n")
        f.write(f""" 
                test_main 
                test-output

                date:       {today}
                version:    0.0.1
                license:    MIT
                \n\n""")
        main(f)
