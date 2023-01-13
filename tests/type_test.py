import unittest

from models.type import Type

class TestType(unittest.TestCase):
    
    def setUp(self):
        self.type_1 = Type("Medical", "/static/images/medical_droid.svg")
    
    def test_type_has_name(self):
        self.assertEqual("Medical", self.type_1.name)
