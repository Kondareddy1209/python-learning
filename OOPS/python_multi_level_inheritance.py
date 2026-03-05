# Example of Multilevel Inheritance in Python

# Base (Grandparent) Class
class konda:
    # Method defined in the base class
    def kondaa(self):
        # Prints a message
        print("kondareddy")


# Derived Class (Parent) inheriting from konda
class DerivedClass(konda):
    # Method defined in the parent class
    def ambavaram(self):
        # Prints a message
        print("ambavaram_konda")


# Second Derived Class (Child) inheriting from DerivedClass
# This creates a multilevel inheritance chain: konda → DerivedClass → DerivedClass1
class DerivedClass1(DerivedClass):
    # Method defined in the child class
    def Tirumala(self):
        # Prints a message
        print("Tirumala_konda")


# Creating an object of the final child class
# The object can access methods from all levels of inheritance
obj = DerivedClass1()

# Calling method from the base class
obj.kondaa()

# Calling method from the parent class
obj.ambavaram()

# Calling method from the child class
obj.Tirumala()