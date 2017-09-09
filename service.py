# type: from typing import List

from model import PointOfInterest
from storage import SQLiteDatabase as Database

""" Module containing classes implementing services. """

class PointOfInterestServices:
	""" Class implementing a service around PointOfInterest. """

	@staticmethod
	def initialize():	# type: () -> None
		""" Initialize the database, creating tables not yet present. """

		Database.initialize()

	@staticmethod
	def add_poi(name, x, y):	# type: (str, int, int) -> None
		""" Store the point at (x, y) named name. """

		Database.add_poi( PointOfInterest(name, x, y) )

	@staticmethod
	def list_pois():	# type: () -> List[str]
		""" Return a list with the name of every stored point. """

		return [poi.name for poi in Database.list_pois()]

	@staticmethod
	def list_nearby(x, y, d_max):	# type: (int, int, int) -> List[str]
		""" Return a list of the names of points that are at most d_max away from (x, y). """

		return [poi.name for poi in Database.list_nearby_pois(x, y, d_max)]
