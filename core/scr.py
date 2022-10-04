from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def contains_poly(a, b) -> bool:
    point = Point(b)
    poligono = Polygon(a)
    return poligono.contains(point)
