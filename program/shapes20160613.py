#hierarchy of shape classes

class Shape:
    def _init_(self, x=0, y=0):
        self.x = x
        self.y = y
    def calc_area(self):
        pass
    def calc_perim(self):
        pass
    def get_shape_type(self):
        return "s"
    def to_string(self):
        return "%s %d %d" % (self.get_shape_type(), self.x, self.y)
class Circle (Shape):
    def _init_(self, x=0,y=0,rad=0):
        super()._init_(x,y)
        self.set_radius(rad)
    def set_radius(self,rad):
        if rad < 0:
            self.radius = 0
        else:
            self.radius = rad
    def calc_area(self):
        return math.pi * math.pow(self.radius,2)
    def calc_perim(self):
        return 2 * math.pi * self.radius
    def get_shape_type(self):
        return "c"
    def to_string(self):
        return "%s %d" % (super().to_string(), self.radius)
class Rectangle(Shape):
    def _init_(self, x=0,y=0,width=0,length=0):
        super()._init_(x,y)
        self.set_width(width)
        self.set_length(length)
    def set_width(self, w):
        if(w<0):
            self.width = o
        else:
                self.width = w
    def set_length(self, ln):
        if(ln < 0):
            self.length = 0
        else:
            self.length = ln
    def calc_area(self):
        return self.length * self.width
    def calc_perim(self):
        return 2 * (self.length + self.width)
    def get_shape_type(self):
        return "r"
    def to_string(self):
        return "%s %d %d" % (super().to_string(), self.width, self.length)
    
class Shape_Printer:
    def __init__(self, shapes):
        self.shapes = shapes
    def print_shapes(self):
        for s in self.shapes:
            print(s.to_string())
            print ("Area = %.3f, Perim = %.3f" %(s.calc_area(), s.calc_perim()))
def main():
    def_cir = Circle()
    alt_cir = Circle(10,20,15)
    def_rec = Rectangle()
    alt_rec = Rectangle(20,30,10,20)
    shapes = [def_cir, alt_cir, def_rec, alt_rec]
    printer = Shape_Printer()
    printer.print_shapes(shapes)
    '''    
    print(def_cir.to_string())
    print(alt_cir.to_string())
    print(def_rec.to_string())
    print(alt_rec.to_string())
    print ("alt_cir has an area of %.3f and a circumference of %.3f" \
           % (alt_cir.calc_area(), alt_circ.carlc_perim()))
    print ("alt_rec has an area of %.3f and a circumference of %.3f" \
           % (alt_rec.calc_area(), alt_rec.calc_perim()))
'''
    
if __name__ == "_main_":
    main()
