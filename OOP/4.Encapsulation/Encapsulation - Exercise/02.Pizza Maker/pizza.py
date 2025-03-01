class Pizza:
  def __init__(self, name, dough, max_number_of_toppings, toppings):
    self.name = name
    self.dough = dough
    self.max_number_of_toppings = max_number_of_toppings
    self.toppings = toppings

   @property
   def name(self):
     return self.__name

   @name.setter
   def name(self, value):
     if value == '':
       raise ValueError("The name cannot be an empty string"

     self.__name = value

    @property
    def dough(self):
      return self.__dough

     @dough.setter
     def dough(self, value):
       if value == "None":
         raise ValueError("You should add dough to the pizza")

        self.__dough = value

      @property
      def max_number_of_toppings(self):
        return self.__max_number_of_toppings

      @max_number_of_toppings.setter
      def max_number_of_toppings(self, value):
        if value <= 0:
          raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        self.__max_number_of_toppings = value

       @property
       def toppings(self):
         return self.__toppings
       
