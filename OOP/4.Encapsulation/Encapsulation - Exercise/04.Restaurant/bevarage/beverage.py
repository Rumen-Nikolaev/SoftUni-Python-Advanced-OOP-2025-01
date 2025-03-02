from project.product import product

class Bevarage(Product):
  def __init__(self, name, price, milliliters):
    super().__init__(name, price)
    self.__milliliters = milliliters

  @property
  def milliliters(self):
    return self.__milliliters

