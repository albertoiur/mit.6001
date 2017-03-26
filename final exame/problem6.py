# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:43:16 2016

@author: ruialberto
"""

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
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)
"""
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)
        
>>> ae.say('the sky is blue')
eric says: It is obvious that eric says: the sky is blue        
"""

class ArrogantProfessor(Professor):
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: It is obvious that ' +   Lecturer.lecture(self,stuff)
        
    def lecture(self, stuff):
        return 'It is obvious that ' +   Lecturer.lecture(self,stuff)
                       
        
e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric') 


'''
It is obvious that I believe that eric says: the sky is blue
'''

       
        