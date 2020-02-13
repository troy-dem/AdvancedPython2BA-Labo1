# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        if utils.fact(0) != 1:
            raise Fact0Error
        if utils.fact(-5) != None:
            raise WrongArgumentError
        if utils.fact("jfeooei") != None:
            raise WrongArgumentError
        if utils.fact(9)!= 362880:
            raise WrongComputationError

    
    def test_roots(self):
        # À compléter...
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
