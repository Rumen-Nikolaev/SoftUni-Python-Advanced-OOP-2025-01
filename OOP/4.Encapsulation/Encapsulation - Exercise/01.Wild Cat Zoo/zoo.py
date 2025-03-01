from project.animal import Animal

class Zoo:
  def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
    self.name = name
    self.__budget = budget
    self.__animal_capacity = animal_capacity
    self._workers_capacity = workers_capacity
    self.animals = []
    self.workers = []

   def add_animal(self, animal: Animal, price):
     if self.__budget < price:
       return "Not enough budget"
     if self.__animal_capacity == len(self.animals):
       return "Not enough space for animal"

     self.animals.append(animal)
     self.__budget -= price

     return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
      

     
     
       
       
     
  
