# ------------------------------------------------
# Example Program: Multiple Inheritance in Python
# ------------------------------------------------

"""
Inheritance Diagram

        konda            kondare
          │                 │
          │                 │
          └───────┬─────────┘
                  │
            DerivedClass
                  │
                 Tiru()

Explanation:
- 'konda' and 'kondare' are parent classes.
- 'DerivedClass' inherits from both parent classes.
- Therefore, DerivedClass can access methods from both parents.
"""

# Parent Class 1
class konda:

    # Method inside the first parent class
    def reddy(self):
        print("Kondareddy")


# Parent Class 2
class kondare:

    # Method inside the second parent class
    def Ambavaram(self):
        print("Tirumala")


# Child Class inheriting from both parent classes
# This demonstrates Multiple Inheritance
class DerivedClass(konda, kondare):

    # Method defined in the child class
    def Tiru(self):
        print("Ambavaram Tirumala Kondareddy")


# Creating an object of the child class
obj = DerivedClass()

# Calling method from Parent Class 1
obj.reddy()

# Calling method from Parent Class 2
obj.Ambavaram()

# Calling method from Child Class
obj.Tiru()