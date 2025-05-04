from math import pi,sqrt
class shape:
  
    def __init__(self,name:str):
       
        if not isinstance(name,str):
            raise TypeError ("name must be a string.")
        self.name=name
    def area(self):
        raise NotImplementedError("subclasses must implement the are method")

    def __str__(self):
        return f"{self.name}"
class Circle(shape):
    def __init__(self,radius:float):
        super().__init__("circle")
        if radius<=0:
            raise ValueError("radius should be positive")
        self.radius=radius
    def area(self):
        return pi * self.radius**2
    def perimeter(self):
        return 2 *pi * self.radius
    def __str__(self):
        return f"{self.name}(radius={self.radius})"
