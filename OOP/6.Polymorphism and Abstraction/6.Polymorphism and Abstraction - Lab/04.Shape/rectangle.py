from shape import Shape

class Rectangle(Shape):
  def __init__(self, height, width):
    self.__height = height
    self.__width = width

  def calculate_area(self):
    return self.__height * self.__width

  def calculate_perimeter(self):
    return 2 * (self.__height + self.__width)
