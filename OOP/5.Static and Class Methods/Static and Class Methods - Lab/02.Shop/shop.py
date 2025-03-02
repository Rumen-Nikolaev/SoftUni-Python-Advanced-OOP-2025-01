class Shop:
  def __init__(self, name, type, capacity):
    self.name = name
    self.type = type
    self.capacity = capacity
    self.items = {}

  @classmethod
  def small_shop(cls, name, type_shop):
    return cls(name, type_shop, 10)

  def add_item(self, item_name):
    if sum(self.items.values()) == self.capacity:
      return "Not enough capacity in the shop"

    if item_name not in self.items:
      self.items[item_name] = 0

    self.items[item_name] += 1

    return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
      
    
