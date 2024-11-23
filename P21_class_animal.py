# create class Animals and create class pet from animal and dog class from pet. and add method to dog class 

class Animals:
    def ani(self):
        print("Animal class")

class Pets(Animals):
    def pet(self):
        print("Pets class")

class Dog(Pets):

    @staticmethod
    def bark():
        print("bow bow!!")

a= Dog()
a.bark()