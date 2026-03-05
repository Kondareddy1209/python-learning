# -------------------------------------------------------
# Example Program: Demonstrating Multiple and Multilevel
# Inheritance in Python
# -------------------------------------------------------

# -------------------------------
# Base Class (Level 1)
# -------------------------------
class Konda:
    # Method inside the base class
    def kondaa(self):
        # This method prints a message
        print("This method belongs to class Konda")


# -------------------------------
# Derived Class (Level 2)
# This inherits from Konda
# → This begins Multilevel Inheritance
# -------------------------------
class Ambavaram(Konda):
    # Method defined in this class
    def ambavaram(self):
        # This method prints a message
        print("This method belongs to class Ambavaram")


# -------------------------------
# Another Independent Parent Class
# This class is not part of the chain
# -------------------------------
class Reddy:
    # Method defined in Reddy class
    def reddy(self):
        # Prints a message
        print("This method belongs to class Reddy")


# -------------------------------
# Final Child Class
# This class inherits from TWO classes:
# 1. Ambavaram
# 2. Reddy
#
# → Ambavaram already inherits from Konda
# → So this forms BOTH:
#    Multilevel + Multiple Inheritance
# -------------------------------
class Tirumala(Ambavaram, Reddy):

    # Method inside the final child class
    def tirumala(self):
        # Prints a message
        print("This method belongs to class Tirumala")


# -------------------------------
# Creating an object of Tirumala
# -------------------------------
obj = Tirumala()

# -------------------------------
# Calling methods from all classes
# -------------------------------

# Method from Konda (grandparent class)
obj.kondaa()

# Method from Ambavaram (parent class)
obj.ambavaram()

# Method from Reddy (second parent class)
obj.reddy()

# Method from Tirumala (child class)
obj.tirumala()