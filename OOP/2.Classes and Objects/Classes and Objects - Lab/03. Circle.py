class Circle:
    pi = 3.14
    
    def __init__(self, radius: int):
        self.radius = radius
        
    def set_radius(self, new_radius: int):
        self.radius = new_radius
        
    def get_area(self):
        return Cicle.pi * (self.radius ** 2)
        
    def get circumference(self):
        return 2 * Circle.pi * self.radius
