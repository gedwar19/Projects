import pymysql
import turtle
import math
#database class connects to the data base
class MySql_Database:
    def __init__(self, server, database, user, pword):
        self.server = server
        self.database = database
        self.user = user
        self.pword = pword
        self.conn = None

    def connect(self):
        try:
            self.conn = pymysql.connect(host = self.server, database = self.database, user = self.user, password = self.pword)
            
            #conn = pymysql.connect(host = "localhost", user = "root", password = "root", database = "shapes_lp245")
        except:
            self.conn = None
        #the execute function will send a query to the connected database
        #return the cursor of results. If the database is not connected, this function will return None



    def execute(self, query):
        if self.conn != None:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor
        else:
            return None
        
    def close(self):
        if self.conn != None:
            self.conn.close()
#location class stores the location information
class Location:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
    def get_draw_params(self):
        return [self.name, self.x, self.y]
    def to_string(self):
        return "%s %.4f %.4f" % (self.name,self.x,self.y)

class MySqlMapData_Fetcher:
    def __init__(self, server="",db="",user="",password=""):
        try:
            self.dbase = MySql_Database(server, db, user, password)
            self.dbase.connect()
        except:
            self.dbase = None
    def is_connected(self):
        if self.dbase == None:
            return False
        else:
            return True
    def get_locations(self, query):
        #this function will return alist of objects that were returned by the query
        cursor = self.dbase.execute(query)
        locations = []
        for (name, xpos, ypos) in cursor:
            loc = Location(name,xpos,ypos)
            locations.append(loc)
        return locations
    def close(self):
        if self.dbase != None:
            self.dbase.close()
#Shape class
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
    def draw_banner(self, title):
        self.x = params[2]*-30+2600
        self.artist.goto(params[2]*-30+2600, params[1]*30-1200)
        self.artist.write(params[0])
    
    
class Turtle_Map_Controller:
    def __init__(self, width, height):
        turtle.setup(width, height)
        self.window = turtle.Screen()
        self.artist = turtle.Turtle()
    
    def draw_map(self, locations):
        self.artist.penup()
        #goes through the list of locations
        for s in locations:
            
            params = s.get_draw_params()
            '''
            print (params[0],math.radians(params[1]*100), math.radians(params[2])*100)
            #print(params[0],params[1]*5, params[2]*5)
            #self.artist.goto(params[1]*5-00, params[2]*5-500)
            self.artist.goto(math.radians(params[1]*100), math.radians(params[2])*100)
            self.artist.pendown()
            input()
            '''
            #reversed the points(lat and long) for the x, and y cordinates
            title = Banner(params[2],params[1], params[0])
            #print(params[0],params[1]*3, params[2]*3)
            #adjusted the ratios to fit on the map with space
            print(params[0], params[2]*-30+2600, params[1]*3-1200)
            self.artist.goto(params[2]*-30+2600, params[1]*30-1200)
            self.artist.write(params[0])
            
    def close(self):
        self.window.bye()
def main():
    server = input("Enter name of database server: ")
    #server = "localhost"
    username = input("Enter your user name: ")
    #username = "root"
    password = input("Enter your password: ")
    #password = "root"
    dbname = input("Enter the name of the database: ")
    #dbname = "map"
    fetch = MySqlMapData_Fetcher(server, dbname, username, password)
    controller = Turtle_Map_Controller(500,500)
    if fetch.is_connected():
        loc_list = fetch.get_locations("select * from midwest")

        if loc_list != None:
            for l in loc_list:
                print(l.to_string())        
        else:
            print("The database is not connected.")
        fetch.close()
    controller.draw_map(loc_list)

if __name__ == "__main__":
    main()
