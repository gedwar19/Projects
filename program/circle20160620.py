#this prgram illustrates declaring private data memebers and accessing them throguh ublic available finctions

class Circle:
    def __init__(self, rad = 0):
        self .set_radius(rad)
    def set_radius(self,rad):
        if rad < 0:
            self.__radius = 0
        else:
            self.__radius = rad
    def get_radius(self):
        return self.__radius
    def to_string(self):
        return "circle with radius %d" % self.__radius
def main():
    def_cir = Circle()
    alt_cir = Circle(5)
    print(def_cir.to_string())
    print (alt_cir.to_string())
    print("The radius of the alt_cir is %d." % alt_cir.get_radius())
    alt_cir.set_radius(2* alt_cir.get_radius())
    print ("After doubling the radius here is the alt_cir:")
    print(alt_cir.to_string())
    
if __name__ == "__main__":
    main()
