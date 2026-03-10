class Animal:
    def __init__(self):
        print("constructer of animal class")

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        print("constructer of dog class")
d = Dog()  # output will show both constructors being called. First, the constructor of the Animal class will run, followed by the constructor of the Dog class.
 # output anedi manam enni class aithe esthamo ani vasati , simpley ga chepali ante ouput lo constructers vastai .