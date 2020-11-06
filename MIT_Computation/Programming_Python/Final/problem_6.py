class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
    def lecture

#class ArrogantProfessor(Professor): 
#    def say(self, stuff): 
#        return 'It is obvious that ' + self.say(stuff)


class ArrogantProfessor(Person):
    def say(self, stuff):
        return  self.name + ' says: ' + 'It is obvious that ' + self.name + ' says: ' + stuff
    
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff






e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

#print(e.say('the sky is blue'))
#print()
#print(le.say('the sky is blue'))
#print()
#print(le.lecture('the sky is blue'))
#print()
#print(pe.say('the sky is blue'))
#print()
print(pe.lecture('the sky is blue'))
print()
print(ae.say('the sky is blue'))
print()
print(ae.lecture('the sky is blue'))
print()
