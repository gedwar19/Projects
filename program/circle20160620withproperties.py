#this prgram illustrates declaring private data memebers and accessing them throguh ublic available finctions
import turtle
class Shape:
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, val):
        self.__x = val
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, val):
        self.__y = val
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def to_string(self):
        return "%s %d %d" % (self.get_shape_type(), self.x, self.y)
    def get_shape_type (self):
        return "s"
    def get_draw_params(self):
        return [self.get_shape_type(), self.x, self.y]
    
    
class Circle(Shape):
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, val):
        if val <0:
            self.__radius = 0
        else:
            self.__radius = val
    def __init__(self, x=0,y=0, rad = 0):
        super().__init__(x,y)
        self.__radius = rad
    def get_shape_type(self):
        return "c"
    def to_string(self):
        return "%s %d" % (super().to_string(), self.radius)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.append(self.radius)
        return result
    #def to_string(self):
     #   return("circle with radius %d" % self.radius)

class Rectangle(Shape):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, val):
        if val < 0:
            self.__width = 0
        else:
            self.__width = val
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, val):
        if val < 0:
            self.__length = 0
        else:
            self.__length = val
    def __init__(self, x =0, y=0, ln= 0, wd = 0):
        super().__init__(x,y)
        self.width = wd
        self.length = ln
    def get_shape_type(self):
        return "r"
    def to_string(self):
        return "%s %d %d " % (super().to_string(), self.width, self.length)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.width, self.length])
        return result
            
# controller class- This will enable us to draw circles and rectangles to a turlte graphics screen
class Turtle_Draw_Shape_Controller:
    def __init__(self, width, height):
        turtle.setup(width, height)
        self.window = turtle.Screen()
        self.artist = turtle.Turtle()
    def (self, width, height):
        self.artist.seth(0)
        for i in range(2):
            self.artist.forward(width)
            self.artist.right(90)
            self.artist.forward(height)
            self.artist.right(90)
            
    def draw_shapes(self, shapes):
        for s in shapes:
            self.artist.penup()
            params = s.get_draw_params()
            '''params[0]= shapetypes, c for circle, r for rectangle
            params[1] = x
            params[2] = y
            for circles, params[3] - radius
            for rects params[3] - width and params [4] - height
            '''
            self.artist.goto(params[1], params[2])
            self.artist.pendown()
            if params[0] == "c":
                self.artist.circle(params[3])
            elif params[0] == "r":
                self.draw_rectangle(params[3], params[4])
    def close(self):
        self.window.bye()
class Shape_IO_Controller:
    def write_file(self, fname, shapes):
        fout = open(fname,"w")
        for s in shapes:
            fout.write("%s\n" %s.to_string())
        fout.close()
    def write_console(self, shapes):
        for s in shapes:
            print(s.to_string())
    def read_file(self, fname):
        fin = open(fname, "r")
        result = []
        for line in fin:
            parts = line.split(" ")
            if parts[0] == "c":
                x = int(parts[1])
                y = int(parts[2])
                rad = int(parts[3])
                shp = Circle(x,y,rad)
            elif parts[0] == "r":
                x = int(parts[1])
                y = int(parts[2])
                length = int(parts[3])
                width  = int(parts[4])
                shp = Rectangle(x,y,length, width)
            else:
                shp = None
            if shp != None:
                result.append(shp)
        fin.close()
        return result
class Face(Rectangle):
    def get_shape_type(self):
        return"f"
    def __init__(self, x=0, y=0, ln = 0, wd = 0):
        super().__init__(x,y,ln,wd)
        super.left_eye = Circle(x+int(0.2*width), y - int(0.2*height), int(0.1*width))
        super.right_eye = Circle(x+int(0.8*width), y - int(0.2*height), int(0.1*width))
    def to_string(self);
        return "%s %s %s" % (super().to_string(), self.left_eye.to_string(),self.right0_eye.to_string())
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend(self.left_eye.get_draw_params())
        result.extend(self.right_eye.get_draw_params())
def main():
    def_cir = Circle()
    alt_cir = Circle(10,20,50)
    print(def_cir.to_string())
    print (alt_cir.to_string())
    print(alt_cir.get_draw_params())
    def_rec = Rectangle()
    alt_rec = Rectangle(50,75,35,78)
    print(def_rec.to_string())
    print(alt_rec.to_string())
    print(alt_rec.get_draw_params())

    tdsc = Turtle_Draw_Shape_Controller(400,400)
    c1 = Circle(0,0,50)
    c2 = Circle(100,100, 25)
    r1 = Rectangle(-100,100,50,100)
    r2 = Rectangle(-100,-100,100,50)
    shapes = [c1,c2,r1,r2]
    tdsc.draw_shapes(shapes)
    input("press enter to continue.")
    tdsc.close()
    print("Going to write the shapes to a file now.")
    sioc = Shape_IO_Controller()
    sioc.write_file("shapes.txt", shapes)
    print("Reading the shapes back in...")
    read_shapes = sioc.read_file("shapes.txt")
    print("these are the shapes that were read..")
    sioc.write_console(read_shapes)
    
if __name__ == "__main__":
    main()

