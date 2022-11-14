#class called circle with variable radius

class circle:
    def __init__(self,radius):
        self.radius = radius

    def __str__(self):
        print("===Cirle===")
        print(f"Radius: {self.radius}")
        print(f"area: {self.area()}")
        print(f"perimeter: {self.circumference()}")

        return ''

    def area(self):
        return ((self.radius*self.radius)*3.14)

    def circumference(self):
        return (2*3.14*self.radius)
