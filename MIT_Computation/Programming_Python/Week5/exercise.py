class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
print(w1.getX())

print(w1.getY())


#The instance does know about x and y as they're its data attributes; their values got assigned when the instance was first created and __init__ method was called subsequently.

#The problem is the getX and getY methods don't actually access that specific instance attributes. They just return values of variables called x and y. And these variables have not been defined anywhere in the code. Not inside the getX, getY or even outside of them. They don't exist.
