import unittest
import movearm
from unittest.mock import MagicMock
from arminit import MoveArm
MoveArm = MagicMock(return_value="from a magic mock!")

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        MoveArm = MagicMock(return_value="from a magic mock!")

    def first_test(self):
        s = 'hello world'
        self.assertEqual(movearm.baseclockwise(), 'test')

if __name__ == '__main__':
    unittest.main()