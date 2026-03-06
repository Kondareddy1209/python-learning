# ------------------------------------------------
# Example Program: Multilevel Inheritance in Python
# ------------------------------------------------

"""
Inheritance Diagram

        konda
          │
          │
      DerivedClass
          │
          │
      DerivedClass2

Explanation:
- 'konda' is the base (parent) class.
- 'DerivedClass' inherits from 'konda'.
- 'DerivedClass2' inherits from 'DerivedClass'.
- This creates a chain of inheritance called Multilevel Inheritance.
"""

# -----------------------------
# Base Class (Level 1)
# -----------------------------
class konda:

    # Method inside base class
    def reddy(self):
        print("konda")


# -----------------------------
# Derived Class (Level 2)
# -----------------------------
# This class inherits from 'konda'
class DerivedClass(konda):

    # Method defined in this class
    def Kondare(self):
        print("Ambavaram")


# -----------------------------
# Second Derived Class (Level 3)
# -----------------------------
# This class inherits from 'DerivedClass'
class DerivedClass2(DerivedClass):

    # Method defined in this class
    def Tirum(self):
        print("Tirumala")


# -----------------------------
# Object Creation
# -----------------------------
# Creating object of the last child class
object = DerivedClass2()

# -----------------------------
# Calling Methods
# -----------------------------

# Method from base class (konda)
object.reddy()

# Method from intermediate class (DerivedClass)
object.Kondare()

# Method from final child class (DerivedClass2)
object.Tirum()