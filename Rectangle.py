from Point import Point
class Rectangle:
    def __init__(self, l , w , point):
        self.width = w
        self.length = l
        self.area_cal_counter = 0
        self.corner = point

    def __repr__(self):
        return f"rectangle with:{self.width} and length:{self.length}"
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.perimeter() > other.perimeter()
    def area(self):
        self.area_cal_counter +=1
        return self.width * self.length
    def perimeter(self):
        return 2*(self.width+self.length)
