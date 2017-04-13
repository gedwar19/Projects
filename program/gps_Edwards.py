import math
#gps calculator class
class GPS_Calculator:
    #function to find the distance
    def calc_distance(self, lat1, long1,lat2, long2):
        self.dlat = math.radians(lat2) - math.radians(lat1) 
        self.dlong = math.radians(long2) - math.radians(long1)
        self.a = math.pow(math.sin(self.dlat/2),2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(self.dlong/2), 2)
        self.c = 2 * math.atan2(math.sqrt(self.a), math.sqrt(1-self.a))
        self.d = 3961 * self.c #3961 is R, the radius of the earth
        #return the disttance in miles
        return self.d
class Report_Printer:
    #print the heads
    def print_Header(self):
        print("---------------------------------------------------------------------")
        print("Time \t\t Latitude \t Longitude     \t Distance     \t Pace")
        print("(hh:mm:ss) \t (deg) \t\t (deg) \t\t (miles) \t (min/mile)")
        print("---------------------------------------------------------------------")
    #print the columns of data
    def print_result(self, first_line, parts, miles, pace):
        if (first_line == True):
            print("%s \t %s \t %s \t ***** \t\t *****" %(parts[0], parts[1], parts[2]) )
        else:
            print("%s \t %s \t %s \t  %.3f \t %.3f" %(parts[0], parts[1], parts[2], miles, pace))
        
#main function   
print("Welcome to Running Mate")
fname = input("Enter the name of the file: ")
print_gps = Report_Printer()
print_gps.print_Header()
#opens the file
fin = open(fname, "r")
latitude =[]
longitude =[]
sec = []
best_pace = 1000
first_line = True
gps = GPS_Calculator()
lat2 = 0.0
lat1 = 0.0
lon2 = 0.0
lon1 = 0.0
time1 = 0
time2 = 0
time3 = 0
miles = 0
pace = 1000
for line in fin:
    line = line.strip()
    if line != "":
        parts = line.split (" ")
        time = parts[0].split(":")
        #for the first run
        if (first_line == True):
            
            lat1 = float(parts[1])
            lon1 = float(parts[2])
            time1 =(int(time[2])+ (int(time[1])*60) +((int(time[0])*60)*60))
            print_gps.print_result(first_line,parts, miles, pace  )
         #for the following updates   
        if (first_line != True):
            lat2 = float(parts[1])
            lon2 = float(parts[2])
            time2 =(int(time[2])+ (int(time[1])*60) +((int(time[0])*60)*60))
            miles = gps.calc_distance(lat1, lon1,lat2, lon2)
            pace = (((time2-time1)/60)/ miles)
            #calls the print class
            print_gps.print_result(first_line,parts, miles, pace)
            #the fastest pace
            if ( pace < best_pace):
                best_pace = pace

        lat1 =lat2
        lon1 =lon2
        time1 = time2
        first_line = False
        
print("The fastest pace was %.3f" %pace)
    
