import unittest
from unittest import TestCase

import M015b

class TestClass(TestCase):
	def testAddiere(self):
		rechner = M015b.Rechner()
		ergebnis = rechner.addiere(4, 5)
		self.assertEqual(ergebnis, 9)

	def testSubtrahiere(self):
		rechner = M015b.Rechner()
		ergebnis = rechner.subtrahiere(4, 5)
		self.assertEqual(ergebnis, -1)

if __name__ == '__main__':
	unittest.main()