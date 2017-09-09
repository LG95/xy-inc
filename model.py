from collections import namedtuple

""" Module containg classes that represent relevant data. """

PointOfInterest = namedtuple("PointOfInterest", "name, x, y")
PointOfInterest.__doc__ = "Class representing points of interest."
