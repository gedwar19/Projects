
class Rectangle:
    def __init__(self, name, x,y,w,h):
        self.name = name
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    def to_string(self):
        return "%s %d %d %d %d" % (self.name, self.x, self.y, self.width, self.height)
