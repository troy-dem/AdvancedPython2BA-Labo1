# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(utils.fact(0),1)
        self.assertIsNone(utils.fact("zetze"))
        self.assertEqual(utils.fact(9),362880)

    
    def test_roots(self):
        # À compléter...
        self.assertEqual(type(utils.roots(1,0,6)),tuple)
        self.assertEqual(utils.roots(1,-2,1),(1,))
        self.assertEqual(utils.roots(1,-4,3),(3,1))
        self.assertEqual(utils.roots(20,1,3),())
    
    def test_integrate(self):
        # À compléter...
        # to test travis
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
