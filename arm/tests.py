import unittest
import movearm
from arminit import MoveArm

def stub():
    'hello'

MoveArm = stub

class TestStringMethods(unittest.TestCase):

    def first_test(self):
        s = 'hello world'
        self.assertEqual(movearm.baseclockwise(), 'test')

if __name__ == '__main__':
    unittest.main()