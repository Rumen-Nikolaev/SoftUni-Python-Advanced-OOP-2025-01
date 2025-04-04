from math import pi
from shape import Shape

class Circle(Shape):
  def __init__(self, radius):
    self.__radius = radius

  def calculate_area(self):
    return pi * (self.__radius ** 2)

  def calculate_perimeter(self):
    return 2 * pi * self.__radius
