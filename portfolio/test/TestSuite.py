import unittest
from portfolio.test import TestAddStock, TestDeleteStock, TestViewPortfolio


loader = unittest.TestLoader()
suite = unittest.TestSuite()


suite.addTest(loader.loadTestsFromModule(TestAddStock))
suite.addTest(loader.loadTestsFromModule(TestDeleteStock))
suite.addTest(loader.loadTestsFromModule(TestViewPortfolio))


runner = unittest.TextTestRunner(verbosity=3)
results = runner.run(suite)