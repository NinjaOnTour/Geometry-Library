import math

def distance(a, b):
    x = abs(a.x - b.x)
    y = abs(a.y - b.y)
    return math.sqrt((x*x) + (y*y))

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

class Line:

    def __init__(self): 
        # ax + by + c = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.tangent = 0

    def constructWithVectors(self, vec1, vec2): 
        # x1 = vec1.x , x2 = vec2.x , y1 = vec1.y , y2 = vec2.y
        # (y1 - y2)/(x1 - x2) = (y - y2)/(x - x2)
        # x(y1 - y2) + y(x2 - x1) + (x1y2 - x2y1) = 0
        # a = y1 - y2 , b = x2 - x1 , c = x1y2 - x2y1
        self.a = vec1.y - vec2.y
        self.b = vec2.x - vec1.x
        self.c = (vec1.x * vec2.y) - (vec2.x * vec1.y)
        self.tangent = -self.a / self.b
    
    def constructWithabc(self, a, b, c):
        # ax + by + c = 0
        self.a = a
        self.b = b
        self.c = c
        self.tangent = -a/b
    
    def getY(self, x): 
        # y = (-ax - c) / b
        return (-self.a*x - self.c) / self.b
    
    def getX(self, y): 
        # x = (-by - c) / a
        return (-self.b*y - self.c) / self.a

    def distanceToPoint(self, vec):
        return abs(self.a * vec.x + self.b * vec.y + self.c) / math.sqrt(self.a * self.a + self.b * self.b)
    
    def distanceToLine(self, line):
        if self.tangent != line.tangent:
            pass

        return abs(self.c - line.c) / math.sqrt(self.a * self.a + self.b * self.b)

class Polygon:

    def __init__(self, edgeCount):
        pass

    def getArea(self):
        pass
