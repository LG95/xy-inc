#!/usr/bin/env python3

from http.client import HTTPConnection
from unittest import main as test, TestCase

from model import PointOfInterest
from service import PointOfInterestServices as Services
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

		self.assertEqual(Database.list_nearby_pois(20, 10, 10),
						 self.__EXPECTED_NEARBY)

class ServicesTest(TestCase):
	""" Class implementing unit tests for service classes. """

	__EXPECTED_NEARBY = ["Lanchonete", "Joalheria", "Pub", "Supermercado"]
	__EXPECTED_LIST = ["Lanchonete", "Posto", "Joalheria", "Floricultura",
					   "Pub", "Supermercado", "Churrascaria"]

	def setUp(self):	# type: () -> None
		""" Prepare the service for tests. """

		Services._initialize()
		Services.add_poi("Lanchonete", "27", "12")
		Services.add_poi("Posto", "31", "18")
		Services.add_poi("Joalheria", "15", "12")
		Services.add_poi("Floricultura", "19", "21")
		Services.add_poi("Pub", "12", "8")
		Services.add_poi("Supermercado", "23", "6")
		Services.add_poi("Churrascaria", "28", "2")

	def test_list_pois(self): 	# type: () -> None
		""" Verify that all inserted points are listed. """

		self.assertEqual(Services.list_pois(), self.__EXPECTED_LIST)

	def test_list_nearby(self): 	# type: () -> None
		""" Verify that the proper nearby points are determined. """

		self.assertEqual(Services.list_nearby("20", "10", "10"),
						 self.__EXPECTED_NEARBY)

class RESTfulTest(TestCase):
	""" Class implementing unit tests for the RESTful service. """

	__BASE_URI = "/xy-inc/points"
	__EXPECTED_NEARBY = ["Lanchonete", "Joalheria", "Pub", "Supermercado"]
	__EXPECTED_LIST = ["Lanchonete", "Posto", "Joalheria", "Floricultura",
					   "Pub", "Supermercado", "Churrascaria"]

	def setUp(self):	# type: () -> None
		""" Prepare the RESTful API for tests. """

		self.__connection = HTTPConnection("localhost", 8080)

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Lanchonete&x=27&y=12")
		self.__connection.getresponse().read()

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Posto&x=31&y=18")
		self.__connection.getresponse().read()

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Joalheria&x=15&y=12")
		self.__connection.getresponse().read()

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Floricultura&x=19&y=21")
		self.__connection.getresponse().read()

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Pub&x=12&y=8")
		self.__connection.getresponse().read()

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Supermercado&x=23&y=6")
		self.__connection.getresponse().read()

		self.__connection.request("GET", self.__BASE_URI + "/add_poi?name=Churrascaria&x=28&y=2")
		self.__connection.getresponse().read()

	def test_list_pois(self): 	# type: () -> None
		""" Verify that all inserted points are listed. """

		self.__connection.request("GET", self.__BASE_URI + "/list_pois")
		response = self.__connection.getresponse().read()

		# remove trailing spaces, convert to string and make a list from each line
		response = str(response.strip(), "utf-8").splitlines()
		self.assertEqual(response, self.__EXPECTED_LIST)

	def test_list_nearby(self): 	# type: () -> None
		""" Verify that the proper nearby points are determined. """

		self.__connection.request("GET", self.__BASE_URI + "/list_nearby?x=20&y=10&d_max=10")
		response = self.__connection.getresponse().read()

		# remove trailing spaces, convert to string and make a list from each line
		response = str(response.strip(), "utf-8").splitlines()
		self.assertEqual(response, self.__EXPECTED_NEARBY)

if __name__ == "__main__": test()
