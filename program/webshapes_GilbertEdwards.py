import urllib.request
import math
import turtle

class Web_Retriever:
    def download(self, url, local_name):
        try:
            retriever = urllib.request.URLopener()
            retriever.retrieve(url,local_name)

            '''
            fin = open(local_name,"r")
            for line in fin:
                print(line)
            fin.close()
            '''
            return True
            
        except:
            return False

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
        return "%s %d %d " % (super().to_string(), self.length, self.width)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.length, self.width])
        return result

class Face(Rectangle):
    def get_shape_type(self):
        return"f"
    def __init__(self, x=0, y=0, ln = 0, wd = 0):
        super().__init__(x,y,ln,wd)
        self.left_eye = Circle(x+int(0.2*ln), y - int(0.2*wd), int(0.1*wd))
        self.right_eye = Circle(x+int(0.8*ln), y - int(0.2*wd), int(0.1*wd))
    def to_string(self):
        return "%s %s %s" % (super().to_string(), self.left_eye.to_string(),self.right_eye.to_string())
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend(self.left_eye.get_draw_params())
        result.extend(self.right_eye.get_draw_params())

class Regular_Polygon(Shape):
    @property
    def sides(self):
        return self.__sides
    @sides.setter
    def sides(self, val):
        if val < 3:
            self.__sides = 3
        else:
            self.__sides = val
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, val):
        if val < 0:
            self.__length = 0
        else:
            self.__length = val
    
    def __init__(self, x =0, y=0, ln= 0, sd = 3):
        super().__init__(x,y)
        self.sides = sd
        self.length = ln
    def get_shape_type(self):
        return "p"
    def to_string(self):
        return "%s %d %d " % (super().to_string(), self.length, self.sides)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.length, self.sides])
        return result
    
class Line(Shape):
    @property
    def x2(self):
        return self.__x2
    @x2.setter
    def x2(self, val):
        self.__x2 = val
    @property
    def y2(self):
        return self.__y2
    @y2.setter
    def y2(self, val):
        self.__y2 = val
    def __init__(self, x =0, y=0, xx= 0, yy = 0):
        super().__init__(x,y)
        self.x2 = xx
        self.y2 = yy
    def get_shape_type(self):
        return "l"
    def to_string(self):
        return "%s %d %d " % (super().to_string(), self.x2, self.y2)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend([self.x2, self.y2])
        return result

class Banner(Shape):
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, word):
        self.__text = word
            
    def __init__(self, x =0, y=0, word = ""):
        super().__init__(x,y)
        self.text = word
    def get_shape_type(self):
        return "b"
    def to_string(self):
        return "%s %s " % (super().to_string(), self.__text)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend(self.__text)
        return result

class House(Rectangle):
    @property
    def roof_height(self):
        return self.__roof_height
    @roof_height.setter
    def roof_height(self, val):
        if val < 0:
            self.__roof_height = 0
        else:
            self.__roof_height = val
            
    def __init__(self, x =0, y=0, ln = 0, wd = 0, h = 0):
        super().__init__(x,y, ln, wd)
        self.roof_height = h
    def get_shape_type(self):
        return "h"
    def to_string(self):
        return "%s %s " % (super().to_string(), self.roof_height)
    def get_draw_params(self):
        result = super().get_draw_params()
        result.extend(self.roof_height)
        return result

class Shape_XML_Parser:
    def parse(self,fname):
        file_var = open(fname,"r")
        text = ""
        for line in file_var:
            text = text + line.strip()
        file_var.close()
        shapes_list = []
        #circle
        pos = text.find("<circle>")
        while pos >= 0:
            endpos = text.find("</circle>",pos+1)
            tagbeg = text.find("<x>",pos+1)
            tagend = text.find("</x>",tagbeg+1)
            x = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<y>",pos+1)
            tagend = text.find("</y>",tagbeg+1)
            y = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<radius>",pos+1)
            tagend = text.find("</radius>",tagbeg+1)
            radius = float(text[tagbeg+8:tagend])
            cir = Circle(radius,x,y)
            shapes_list.append(cir)
            pos = text.find("<circle>",endpos+9)
        #finds rectangle data
        pos = text.find("<rectangle>")
        while pos >= 0:
            endpos = text.find("</rectangle>",pos+1)
            tagbeg = text.find("<x>",pos+1)
            tagend = text.find("</x>",tagbeg+1)
            x = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<y>",pos+1)
            tagend = text.find("</y>",tagbeg+1)
            y = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<length>",pos+1)
            tagend = text.find("</length>",tagbeg+1)
            length = float(text[tagbeg+8:tagend])
            tagbeg = text.find("<width>",pos+1)
            tagend = text.find("</width>",tagbeg+1)
            width = float(text[tagbeg+7:tagend])
            rec = Rectangle(x,y,length,width)
            shapes_list.append(rec)
            pos = text.find("<rectangle>",endpos+12)
        #finds face data
        pos = text.find("<face>")
        while pos >= 0:
            endpos = text.find("</face>",pos+1)
            tagbeg = text.find("<x>",pos+1)
            tagend = text.find("</x>",tagbeg+1)
            x = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<y>",pos+1)
            tagend = text.find("</y>",tagbeg+1)
            y = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<length>",pos+1)
            tagend = text.find("</length>",tagbeg+1)
            length = float(text[tagbeg+8:tagend])
            tagbeg = text.find("<width>",pos+1)
            tagend = text.find("</width>",tagbeg+1)
            width = float(text[tagbeg+7:tagend])
            fac = Face(x,y,length,width)
            shapes_list.append(fac)
            pos = text.find("<face>",endpos+7)
        #finds regularpolygon data
        pos = text.find("<regpoly>")
        while pos >= 0:
            endpos = text.find("</regpoly>",pos+1)
            tagbeg = text.find("<x>",pos+1)
            tagend = text.find("</x>",tagbeg+1)
            x = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<y>",pos+1)
            tagend = text.find("</y>",tagbeg+1)
            y = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<length>",pos+1)
            tagend = text.find("</length>",tagbeg+1)
            length = float(text[tagbeg+8:tagend])
            tagbeg = text.find("<sides>",pos+1)
            tagend = text.find("</sides>",tagbeg+1)
            sides = float(text[tagbeg+7:tagend])
            pol = Regular_Polygon(x,y,length,sides)
            shapes_list.append(pol)
            pos = text.find("<regpoly>",endpos+10)
        #finds house data
        pos = text.find("<line>")
        while pos >= 0:
            endpos = text.find("</line>",pos+1)
            tagbeg = text.find("<x1>",pos+1)
            tagend = text.find("</x1>",tagbeg+1)
            x = float(text[tagbeg+4:tagend])
            tagbeg = text.find("<y1>",pos+1)
            tagend = text.find("</y1>",tagbeg+1)
            y = float(text[tagbeg+4:tagend])
            tagbeg = text.find("<x2>",pos+1)
            tagend = text.find("</x2>",tagbeg+1)
            x2 = float(text[tagbeg+4:tagend])
            tagbeg = text.find("<y2>",pos+1)
            tagend = text.find("</y2>",tagbeg+1)
            y2 = float(text[tagbeg+4:tagend])
            lin = Line(x,y,x2,y2)
            shapes_list.append(lin)
            pos = text.find("<line>",endpos+7)
        #finds banner data
        pos = text.find("<banner>")
        while pos >= 0:
            endpos = text.find("</banner>",pos+1)
            tagbeg = text.find("<x>",pos+1)
            tagend = text.find("</x>",tagbeg+1)
            x = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<y>",pos+1)
            tagend = text.find("</y>",tagbeg+1)
            y = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<text>",pos+1)
            tagend = text.find("</text>",tagbeg+1)
            text = text[tagbeg+6:tagend]
            ban = Banner(x,y,text)
            shapes_list.append(ban)
            pos = text.find("<banner>",endpos+9)
        #finds house data
        pos = text.find("<house>")
        while pos >= 0:
            endpos = text.find("</house>",pos+1)
            tagbeg = text.find("<x>",pos+1)
            tagend = text.find("</x>",tagbeg+1)
            x = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<y>",pos+1)
            tagend = text.find("</y>",tagbeg+1)
            y = float(text[tagbeg+3:tagend])
            tagbeg = text.find("<length>",pos+1)
            tagend = text.find("</length>",tagbeg+1)
            length = float(text[tagbeg+8:tagend])
            tagbeg = text.find("<width>",pos+1)
            tagend = text.find("</width>",tagbeg+1)
            width = float(text[tagbeg+7:tagend])
            tagbeg = text.find("<roof>",pos+1)
            tagend = text.find("</roof>",tagbeg+1)
            roof = float(text[tagbeg+6:tagend])
            hos = House(x,y,length,width, roof)
            shapes_list.append(hos)
            pos = text.find("<house>",endpos+8)
        return shapes_list

# controller class- This will enable us to draw circles and rectangles to a turlte graphics screen
class Turtle_Draw_Shape_Controller:
    def __init__(self, width, height):
        turtle.setup(width, height)
        self.window = turtle.Screen()
        self.artist = turtle.Turtle()
    def draw_rectangle(self, length, width):
        self.artist.seth(0)
        for i in range(2):
            self.artist.forward(length)
            self.artist.right(90)
            self.artist.forward(width)
            self.artist.right(90)
            
    '''length,height,-rectangles length and height
    lex, ley, ler,- the left circles (x,y, radius)
    rex,rey, rer- the right circles (x,y, radius)
    '''
    def draw_face(self, length, width, lex, ley, ler, rex,rey, rer):
        self.draw_rectangle(length, width)
        #left circle
        self.artist.penup()
        self.artist.goto(lex, ley)
        self.artist.pendown()
        self.artist.circle(ler)
        #right circle
        self.artist.penup()
        self.artist.goto(rex, rey)
        self.artist.pendown()
        self.artist.circle(rer)
     #connects to (x2,y2)   
    def draw_line(self,x2,y2):
        self.artist.goto(x2, y2)
        
    def draw_house(self, length, width, height):
        self.draw_rectangle(length, width)
        self.artist.penup()
        self.artist.goto(self.x, (self.y + width))
        self.artist.pendown()
        draw_line(length+(length/2), (width+height))
        draw_line( length+(length/2), (width-height))
        
    def draw_regular_polygon(self, length, sides):
        for i in range(sides +1):
            self.artist.forward(length)
            self.artist.right((360/sides))
            
    def draw_shapes(self, shapes):
        for s in shapes:
            self.artist.penup()
            params = s.get_draw_params()
            '''params[0]= shapetypes, c for circle, r for rectangle
            params[1] = x
            params[2] = y
            for circles, params[3] - radius
            for rects params[3] - width and params [4] - height
            for face params[3] - rec width and params [4] - rec height,
            params [5]- left eye x, params [6]- left eye y,params [7]- left eye radius,
            params [8]- right eye x, params [9]- right eye y,params [10]- right eye radius
            '''
            self.artist.goto(params[1], params[2])
            self.artist.pendown()
            if params[0] == "c":
                self.artist.circle(params[3])
            elif params[0] == "r":
                self.draw_rectangle(params[3], params[4])
            elif params[0] == "f":
                self.draw_face(params[3], params[4], params[6], params[7], params[8], params[10], params[11], params[12], )
            elif params[0] == "l":
                self.draw_line(params[3], params[4])
            elif params[0] == "h":
                self.draw_house(params[3], params[4], params[5])
            elif params[0] == "b":
                Banner(params[3])
                Banner.to_string()
            elif params[0] == "p":
                self.draw_regular_polygon(params[3], params[4])
                
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
            #parse the data into shape types
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
            elif parts[0] == "f":
                x = int(parts[1])
                y = int(parts[2])
                length = int(parts[3])
                width  = int(parts[4])
                shp = Face(x,y,length, width)
            elif parts[0] == "p":
                x = int(parts[1])
                y = int(parts[2])
                length = int(parts[3])
                side  = int(parts[4])
                shp = Regular_Polygon(x,y,length, side)
            elif parts[0] == "l":
                x = int(parts[1])
                y = int(parts[2])
                x2 = int(parts[3])
                y2  = int(parts[4])
                shp = Line(x,y,x2, y2)
            elif parts[0] == "b":
                x = int(parts[1])
                y = int(parts[2])
                word = parts[3]
                shp = Banner(x,y,word)
            elif parts[0] == "h":
                x = int(parts[1])
                y = int(parts[2])
                length = int(parts[3])
                width  = int(parts[4])
                height = int(parts[5])
                shp = House(x,y,length, width, height)
            else:
                shp = None
            if shp != None:
                result.append(shp)
        fin.close()
        return result
    
def main():
    
    url = input("Enter url of shapes file: ")
    file = input("Enter name of file to save locally: ")

    #url = "http://cs.lewisu.edu/~klumpra/2016Summer/shapes.xml"
    #file = "test_shapes.xml"
    wrt = Web_Retriever()
    parser = Shape_XML_Parser()
    controller = Turtle_Draw_Shape_Controller(500,500)
    if wrt.download(url, file) == True:
        print ("success")
        shape = parser.parse(file)
        Shape_IO_Controller().write_console(shape)
        Shape_IO_Controller().write_file(file, shape)
        shape2 = Shape_IO_Controller().read_file(file)
        Shape_IO_Controller().write_console(shape2)
        controller.draw_shapes(shape)
    else:
        print("Something went wrong.")
    
    reader = Shape_XML_Parser()
    #if reader != None:
        
    
    

if __name__ == "__main__":
    main()
