import random
import unittest
import functions
from mock import patch


class TestMethods(unittest.TestCase):

    def test_all_available(self):
        mode = 0 # all_available
        issue = {'role': ["hindi", "sales"]}
        self.assertEqual(functions.selection(mode, issue), ['agent3', 'agent7'])

    def test_least_busy(self):
        mode = 1 # least_busy
        issue = {'role': ["hindi"]}
        self.assertEqual(functions.selection(mode, issue), ['agent7'])

    @patch('functions.random')
    def test_random(self, random):
        mode = 2 # random
        issue = {'role': ["hindi"]}
        self.assertEqual(functions.selection(mode, issue), ['agent3'] or ['agent7'])
