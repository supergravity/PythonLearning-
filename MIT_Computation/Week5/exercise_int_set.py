class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        self.new = [] 
        for i in self.vals:
            for j in other.vals:
                if (i == j):
                    self.new.append(i)
        #return self.new
        return '{' + ','.join([str(e) for e in self.new]) + '}'


    def __len__(self):
        """Returns the number of elements in the set(object)"""
        return len(self.vals)


set1 = intSet()
set1.insert(4)
set1.insert(7)
print(set1)

set2 = intSet()
set2.insert(8)
set2.insert(9)
print(set2)

print(set1.intersect(set2))

print(set1.__len__())
print(len(set1))
