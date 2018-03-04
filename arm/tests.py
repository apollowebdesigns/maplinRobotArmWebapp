from django.test import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch

def stub():
    return 'hello'

class ArmTestCase(TestCase):
    def setUp(self):

    def test_animals_can_speak(self):
        self.assertEqual(stub(), 'The lion says "roar"')