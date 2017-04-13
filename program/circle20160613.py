#Gilbert
#example of how to create a class

import math
import random
class Circle:
        def _init_(self, rad = 0):
            self.radius = rad
        def to_string(self):
            return "c %.3f" % self.radius
        def calc_area(self):
            return math.pi * self.radius * self.radius
        #could have use math.pow(self.radius, 2)
        def calc_perim(self):
            return 2 * math.pi * self .radius

def main();
    rad = random.randint(1,25)
    c1 = Circle(rad)
    c2 = Circle()
    print(c1.to_string())
    print(c1.tp_string())
    print('the area of c1 is %.3f, and the perim is %.3f ' % c1.calc_area(), c1)
if _name_ == "_main_":
    main()
