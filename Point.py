from color import Color
class Point():
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.Color = c
    def __repr__(self):
        return (f"point with x:{self.x} and y:{self.y}"
                f"and color:{self.Color}")
