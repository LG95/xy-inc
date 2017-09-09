#!/usr/bin/env python

from unittest import main as test, TestCase

from model import PointOfInterest
from storage import SQLiteDatabase as Database

""" Module containing classes implementing unit tests. """

class DatabaseTest(TestCase):
	""" Class implementing unit tests for database classes. """

	__LANCHONETE = PointOfInterest("Lanchonete", 27, 12)
	__POSTO = PointOfInterest("Posto", 31, 18)
	__JOALHERIA = PointOfInterest("Joalheria", 15, 12)
	__FLORICULTURA = PointOfInterest("Floricultura", 19, 21)
	__PUB = PointOfInterest("Pub", 12, 8)
	__SUPERMERCADO = PointOfInterest("Supermercado", 23, 6)
	__CHURRASCARIA = PointOfInterest("Churrascaria", 28, 2)

	__EXPECTED_NEARBY = [__LANCHONETE, __JOALHERIA, __PUB, __SUPERMERCADO]
	__EXPECTED_LIST = [__LANCHONETE, __POSTO, __JOALHERIA, __FLORICULTURA,
					   __PUB, __SUPERMERCADO, __CHURRASCARIA]

	def setUp(self):	# type: () -> None
		""" Prepare the database for tests. """

		Database.initialize()
		Database.add_poi(self.__LANCHONETE)
		Database.add_poi(self.__POSTO)
		Database.add_poi(self.__JOALHERIA)
		Database.add_poi(self.__FLORICULTURA)
		Database.add_poi(self.__PUB)
		Database.add_poi(self.__SUPERMERCADO)
		Database.add_poi(self.__CHURRASCARIA)

	def test_list_pois(self):	# type: () -> None
		""" Verify that all inserted points are listed. """

		self.assertEqual(Database.list_pois(), self.__EXPECTED_LIST)

	def test_list_nearby_pois(self):	# type: () -> None
		""" Verify that the proper nearby points are determined. """

		self.assertEqual(Database.list_nearby_pois(20, 10, 10), self.__EXPECTED_NEARBY)

if __name__ == '__main__': test()
