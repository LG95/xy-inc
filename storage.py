from math import sqrt
from sqlite3 import connect, IntegrityError
# type: from typing import List

from model import PointOfInterest as POI

""" Module containing classes to persist data. """

class SQLiteDatabase:
	""" Class implementing persistence using SQLite. """

	__NAME = "points.db"

	@classmethod
	def initialize(cls):	# type: () -> None
		""" Initialize the database, creating tables not yet present. """

		with connect(cls.__NAME) as connection:
			connection.execute("""CREATE TABLE IF NOT EXISTS PointsOfInterest
								(name STRING PRIMARY KEY, x INTEGER, y INTEGER);""")

	@classmethod
	def add_poi(cls, poi):	# type: (POI) -> None
		""" Store poi in the database. """

		try:
			with connect(cls.__NAME) as connection:
				connection.execute("INSERT INTO PointsOfInterest VALUES (?, ?, ?);",
								   (poi.name, poi.x, poi.y))
		except IntegrityError: pass

	@classmethod
	def list_pois(cls):	# type: () -> List[POI]
		""" Return a list with every point in the database. """

		with connect(cls.__NAME) as connection:
			cursor = connection.cursor()
			cursor.execute("SELECT name, x, y FROM PointsOfInterest;")
			return [POI._make(data) for data in cursor]

	@classmethod
	def list_nearby_pois(cls, x, y, d_max):	# type: (int, int, int) -> List[POI]
		""" Return a list of points that are at most d_max away from (x, y). """

		with connect(cls.__NAME) as connection:
			cursor = connection.cursor()
			cursor.execute("SELECT name, x, y FROM PointsOfInterest;")
			return [POI(name, px, py) for name, px, py in cursor
					if sqrt((px - x) ** 2 + (py - y) ** 2) <= d_max]
