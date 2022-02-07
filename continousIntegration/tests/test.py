import unittest
import sys
import os
sys.path.append('../')
from modules.test import test 


class Tests(unittest.TestCase):
    '''
    ''' 
    def test1(self):
        status , _ = test('./test1')
        self.assertTrue(status == 'SUCCESS')

    def test2(self):
        status , _ = test('./test2')
        self.assertTrue(status == 'SUCCESS')

    def test3(self):
        status , _ = test('./test3')
        self.assertTrue(status == 'ERROR')
    

if __name__ == '__main__':
    unittest.main()