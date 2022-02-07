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
        

if __name__ == '__main__':
    unittest.main()