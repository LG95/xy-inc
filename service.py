# type: from typing import List

from model import PointOfInterest
from storage import SQLiteDatabase as Database

""" Module containing classes implementing services. """

class PointOfInterestServices:
	""" Class implementing a service around PointOfInterest. """

	@staticmethod
	def _initialize():	# type: () -> None
		""" Initialize the database, creating tables not yet present. """

		Database.initialize()

	@staticmethod
	def add_poi(name, x, y):	# type: (str, str, str) -> None
		""" Store the point at (x, y) named name. """

		assert x.isdigit(), x + " is not an integer"
		assert y.isdigit(), y + " is not an integer"
		Database.add_poi( PointOfInterest(name, int(x), int(y)) )

	@staticmethod
	def list_pois():	# type: () -> List[str]
		""" Return a list with the name of every stored point. """

		return [poi.name for poi in Database.list_pois()]

	@staticmethod
	def list_nearby(x, y, d_max):	# type: (str, str, str) -> List[str]
		""" Return a list of the names of points that are at most d_max away from (x, y). """

		assert x.isdigit(), x + " is not an integer"
		assert y.isdigit(), y + " is not an integer"
		assert d_max.isdigit(), d_max + " is not an integer"
		return [poi.name for poi in Database.list_nearby_pois(int(x), int(y), int(d_max))]
