# Example of Multiple Inheritance in Python

# Parent Class 1
class konda:
    # Method inside class konda
    def konda(self):
        # This method prints a message
        print("kondareddy")


# Parent Class 2
class reddy:
    # Method inside class reddy
    def ambavaram(self):
        # This method prints a message
        print("ambavaram_konda")


# Child Class inheriting from both konda and reddy
# This is called Multiple Inheritance
class DerivedClass(konda, reddy):

    # Method defined inside the child class
    def Tirumala(self):
        # This method prints a message
        print("Tirumala_konda")


# Creating an object of DerivedClass
# The object can access methods from both parent classes and its own class
obj = DerivedClass()

# Calling method from Parent Class 1
obj.konda()

# Calling method from Parent Class 2
obj.ambavaram()

# Calling method from Child Class
obj.Tirumala()