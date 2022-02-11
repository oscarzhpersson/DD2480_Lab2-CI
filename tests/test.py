import unittest
import os
import sys

sys.path.append('continousIntegration/modules')
import compilation

class Test(unittest.TestCase):
    '''
    ''' 
    def test(self):
        self.assertTrue(os.path.isdir('../DD2480_LAB2-CI'))

    def test_Compile(self):
        print("Prolog")
        compilation.compile(os.getcwd())
        

if __name__ == '__main__':
    unittest.main()