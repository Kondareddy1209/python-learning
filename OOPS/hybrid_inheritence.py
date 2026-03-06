# ------------------------------------------------
# Example Program: Hybrid Inheritance in Python
# ------------------------------------------------

"""
Inheritance Diagram

            ramana
           /     \
          /       \
DerivedClass1   DerivedClass2
       \            /
        \          /
       FinalDerivedClass

Explanation:
- 'ramana' is the base (parent) class.
- 'DerivedClass1' and 'DerivedClass2' inherit from 'ramana'.
  → This is Hierarchical Inheritance.
- 'FinalDerivedClass' inherits from both 'DerivedClass1' and 'DerivedClass2'.
  → This is Multiple Inheritance.
- Combining both forms Hybrid Inheritance.
"""

# -----------------------------
# Base Class (Parent)
# -----------------------------
class ramana:

    # Method in parent class
    def reddy(self):
        print("Father")


# -----------------------------
# First Child Class
# -----------------------------
class DerivedClass1(ramana):

    # Method specific to this class
    def poo(self):
        print("daughter")


# -----------------------------
# Second Child Class
# -----------------------------
class DerivedClass2(ramana):

    # Method specific to this class
    def konda(self):
        print("Son")


# -----------------------------
# Final Child Class
# -----------------------------
# This class inherits from both DerivedClass1 and DerivedClass2
class FinalDerivedClass(DerivedClass1, DerivedClass2):

    # Method specific to this class
    def siddamma(self):
        print("Mother")


# -----------------------------
# Object Creation
# -----------------------------
obj = FinalDerivedClass()

# Calling method from parent class
obj.reddy()

# Calling method from DerivedClass1
obj.poo()

# Calling method from DerivedClass2
obj.konda()

# Calling method from FinalDerivedClass
obj.siddamma()