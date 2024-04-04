#This file is for the creation of basic classes and practice of classes in Python.

#This is a basic class just to test some methodologies, refamiliarize myself with some basic python, and have some fun
class Cadet:

    #Like a construction, also creates attributes of the class
    def __init__(self, name, grade, major): 
        self.name = input("What is the Cadet's name? ")
        self.grade = input("What is the MS level of the Cadet? ")
        self.major = input("What is the major of the Cadet? ")

#Practice creation of an instance of the class
person = Cadet(1, 2, 3) 

#Output information about the created object
print("The cadet's name is " + person.name + ", his or her MS level is " + person.grade + ", and his or her major is " + person.major)
