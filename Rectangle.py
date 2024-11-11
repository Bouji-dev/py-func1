from Point import Point
from color import Color
class Rectangle:
    def __init__(self, l , w , Point , Color):
        self.width = w
        self.length = l
        self.area_cal_counter = 0
        self.corner = Point
        self.Color = Color

    def __repr__(self):
        return (f"rectangle with width:{self.width} and length:{self.length}"
                f" and point{self.corner}  and color:{self.Color}")
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.perimeter() > other.perimeter()
    def area(self):
        self.area_cal_counter +=1
        return self.width * self.length
    def perimeter(self):
        return 2*(self.width+self.length)