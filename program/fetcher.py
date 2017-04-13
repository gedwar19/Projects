from rect import Rectangle
from database import MySql_Database

class MySql_Rectangle_Data_Fetcher:
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
    def get_data(self, query):
        #this function will return alist of rectangles that were returned by the query
        cursor = self.dbase.execute(query)
        rectangles = []
        for (name, xpos, ypos, width, height) in cursor:
            rec = Rectangle(name,xpos,ypos,width,height)
            rectangles.append(rec)
        return rectangles
    def close(self):
        if self.dbase != None:
            self.dbase.close()
