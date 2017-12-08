import unittest
import hometask6

class TestHometask6(unittest.TestCase):

    def test_len_output_json(self):
        self.assertGreater(len(hometask6.json_output), 0)

    def test_type_of_output_json(self):
        self.assertIs(type(hometask6.python2(hometask6.source2, 'system')), dict)
