import unittest
from tests import TestGreeting

suite = unittest.TestSuite()
# List test classes you wish to run in the tests variable
tests = [TestGreeting.TestGreeting, ]
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)