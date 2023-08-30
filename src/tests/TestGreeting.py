import unittest
from greeting import getGreeting

class TestGreeting(unittest.TestCase):
    def testGetGreeting(self):
        self.assertEqual(getGreeting(), "Greetings, User!")
        self.assertEqual(getGreeting("Bob"), "Greetings, Bob!")

if __name__ == '__main__':
    unittest.main()