from math import sqrt, pi

class Fig():

    def fig_area(self):
        pass

    def fig_perimeter(self):
        pass

class Circle(Fig):
    def __init__(self, radius):
        self.radius = radius
        

    def fig_area(self):
        area = self.radius ** 2 * pi
        return(area)
    
class Triangle(Fig):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def fig_perimeter(self):
        return self.a + self.b + self.c     
            

    def fig_area(self):
        perimeter_half = self.fig_perimeter() / 2
        area = sqrt(perimeter_half * (perimeter_half - self.a) * (perimeter_half - self.b) * (perimeter_half - self.c))
        return area
    
    def is_right(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            return "Прямоугольный."
        return "Не Прямоугольный."
    

def fig_area(*args):
    if len(args) == 1:
        return Circle(*args).fig_area()
    
    if len(args) == 3:
        return Triangle(*args).fig_area()




