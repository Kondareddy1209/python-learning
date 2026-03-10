class Animal:
    def __init__(self):
        print("constructer of animal class")

class Dog(Animal):
    def __init__(self):
        print("constructer of dog class")
# d = Animal()
d=Dog()  # output will chage according to the class which we are creating object of. if we create object of dog class then constructer of dog class will run and if we create object of animal class then constructer of animal class will run. 
#simplly creeating object ni call chesthe constructer of that class run avtundi