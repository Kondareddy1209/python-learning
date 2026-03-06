# ------------------------------------------------
# Example Program: Hierarchical Inheritance
# ------------------------------------------------

"""
Inheritance Diagram

           konda
          /     \
         /       \
DerivedClass   DerivedClass1

Explanation:
- 'konda' is the parent class.
- 'DerivedClass' and 'DerivedClass1' are child classes.
- Both child classes inherit from the same parent.
"""

# Parent Class
class konda:

    # Method inside parent class
    def reddy(self):
        print("kondareddy")


# First Child Class
class DerivedClass(konda):

    # Method specific to this child class
    def kondare(self):
        print("Kondareddy_Ambavaram")


# Second Child Class
class DerivedClass1(konda):

    # Method specific to this child class
    def Tiruma(self):
        print("Ambavaram Tirumala Kondareddy")


# Creating object of first child class
object1 = DerivedClass()

# Calling parent method
object1.reddy()

# Calling method of DerivedClass
object1.kondare()


# Creating object of second child class
object2 = DerivedClass1()

# Calling parent method
object2.reddy()

# Calling method of DerivedClass1
object2.Tiruma()