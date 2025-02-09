# Object Oriented Programming

class Car:
    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # a method function
    def dream_car(self):
        print(f"My dream car is a {self.make} {self.model} from  {self.year}")

# create object or instance of a class

myobj = Car("Ford", "Mustang", 1999)
myobj2 = Car("Ferrari", "950", 2010)

myobj.dream_car()
myobj2.dream_car()