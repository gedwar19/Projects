import pymysql

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
