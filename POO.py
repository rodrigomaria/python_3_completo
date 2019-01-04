class Line(object):    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        xa,ya = self.coor1
        xb,yb = self.coor2
        d =((xb-xa)**2)+((yb-ya)**2)
        return d**0.5        
    
    def slope(self):
        xa,ya = self.coor1
        xb,yb = self.coor2
        return (yb-ya)/(xb-xa)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print ('Distancia =', li.distance())

print ('Diagonal =', li.slope())


class Cylinder(object):
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return Cylinder.pi * (self.radius**2) * self.height
    
    def surface_area(self):
        ai = 2 * Cylinder.pi * self.radius * self.height
        return 2 * (Cylinder.pi * (self.radius**2)) + ai

c = Cylinder(2,3)

print ('Volume do Cilindro =', c.volume())

print ('Area do Cilindro =', c.surface_area())