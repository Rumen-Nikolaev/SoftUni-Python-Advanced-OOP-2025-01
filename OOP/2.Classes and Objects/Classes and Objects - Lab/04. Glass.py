class Glass:
    capacity = 250
    
    def __init__(self):
        self.content = 0
        
    def fill(self, ml):
        if self.content + ml <= Glas.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"
        
    def empty(self):
        self.content = 0
        return "Glass is now empty"
        
    def info(self):
        space_left = Glass.capacity - self.content
        return f"{space_left} ml left"
    
        
        
