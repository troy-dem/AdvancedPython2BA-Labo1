# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class Fact0Error(Exception):
    pass
class Fact0Error(Exception):
    pass
class WrongArgumentError(Exception):
    pass
class WrongComputationError(Exception):
    pass
class WrongReturnTypeError(Exception):
    pass


class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        if utils.fact(0) != 1:
            raise Fact0Error()
        if utils.fact("jfeooei") != None:
            raise WrongArgumentError()
        if utils.fact(9)!= 362880:
            raise WrongComputationError()

    
    def test_roots(self):
        # À compléter...
        if type(utils.roots(1,0,2)) != tuple:
            raise WrongReturnTypeError()
        if utils.roots(1,-2,1)!=(1,):
            raise WrongComputationError()
        if utils.roots(1,-4,3)!=(3,1):
            raise WrongComputationError()
        if utils.roots(20,1,3)!=():
            raise NegativeDelataError()
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
