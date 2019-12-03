from math import sqrt, asin

class Triangle():
    
    """
    Simple class for triangle by 3 sides
    """
    
    def calcP(self):
        return self.a + self.b + self.c
    
    def calcS(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b+ c) / 2
        S = sqrt(p * (p - a) * (p - b) * p - c)
        return S
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    
class IsoTriangle(Triangle):
    
    def calcH(self):
        return self.calcS() * 2 / self.a
    
    def calcCorner(self, a, b):
        S = self.calcS
        sinA = S * 2 / (a * b)
        A = asin(sinA)
        return A
    
    def __init__(self, a, b):
        Triangle.__init__(a, b, b)
        
    