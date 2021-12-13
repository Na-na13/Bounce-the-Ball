import unittest

from clock import Clock

class TestClock(unittest.TestCase):
    def setUp(self):
        self.testclock = Clock()
    
    def test_get_ticks(self):
        self.assertEqual(self.testclock.clock_get_ticks(), 0)