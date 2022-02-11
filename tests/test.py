import unittest
import os

class Test(unittest.TestCase):
    '''
    ''' 
    def test(self):
        self.assertTrue(os.path.isdir('../DD2480_LAB2-CI'))

    def test(self):
        self.assertTrue(os.path.isdir('../.TOKEN.txt'))

if __name__ == '__main__':
    unittest.main()