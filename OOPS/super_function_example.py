# -------------------------------------------------------------
# PYTHON INHERITANCE EXAMPLE WITH super()
# Author: Learning Example
#
# This file demonstrates:
# 1. Constructor inheritance using super()
# 2. Method overriding using super()
# 3. Common mistakes beginners make and how to fix them
# -------------------------------------------------------------


# =============================================================
# EXAMPLE 1: USING super() WITH CONSTRUCTORS (__init__)
# =============================================================

# Parent Class
class konda:
    # Constructor to initialize the name
    def __init__(self, name):
        self.name = name


# Child Class inheriting from konda
class amba(konda):

    # Child constructor
    def __init__(self, name, age):

        # super() calls the parent class constructor
        # This initializes the variable "name"
        super().__init__(name)

        # New attribute specific to child class
        self.age = age


# Creating object of child class
emp = amba("kondareddy", 20)

# Accessing inherited and child attributes
print(emp.name)
print(emp.age)


# -------------------------------------------------------------
# EXPECTED OUTPUT
# kondareddy
# 20
# -------------------------------------------------------------



# =============================================================
# EXAMPLE 2: METHOD OVERRIDING WITH super()
# =============================================================

# Parent class
class konda:
    # Method to store name
    def reddy(self, name):
        self.name = name


# Child class inheriting from konda
class amba(konda):

    # Method overriding
    # This method has the same name as the parent method
    def reddy(self, name, age):

        # super() calls the parent class method
        # This sets the "name"
        super().reddy(name)

        # Child class adds a new attribute
        self.age = age


# Creating object
emp = amba()

# Calling overridden method
emp.reddy("kondareddy", 20)

# Printing values
print(emp.name)
print(emp.age)


# -------------------------------------------------------------
# EXPECTED OUTPUT
# kondareddy
# 20
# -------------------------------------------------------------



# =============================================================
# MISTAKES I MADE WHILE LEARNING
# =============================================================

# ❌ Mistake 1: Passing parameters while creating object
# when class does not have __init__

# WRONG
# emp = amba("kondareddy",20)

# WHY?
# Because Python automatically calls __init__ when an object
# is created. If __init__ is not defined, Python's default
# constructor does not accept arguments.

# ✔ FIX
# emp = amba()
# emp.reddy("kondareddy",20)



# -------------------------------------------------------------

# ❌ Mistake 2: Calling method without object

# WRONG
# emp = reddy("kondareddy",20)

# WHY?
# reddy() is a class method, not a global function.

# ✔ FIX
# emp.reddy("kondareddy",20)



# -------------------------------------------------------------

# ❌ Mistake 3: Using super() when parent has no method

# Example WRONG usage
# super().__init__(name)

# If parent class does not define __init__,
# Python will raise an error.

# ✔ FIX
# Ensure parent method exists before calling super()



# =============================================================
# COMMON BEGINNER MISTAKES WITH super() AND INHERITANCE
# =============================================================

# 1️⃣ Forgetting to call parent constructor
# This results in missing attributes.

# 2️⃣ Passing wrong number of parameters to super()

# 3️⃣ Not understanding that super() follows
# Python's Method Resolution Order (MRO)

# Example to check MRO:
# print(amba.mro())



# =============================================================
# KEY CONCEPTS DEMONSTRATED
# =============================================================

# 1. Inheritance
# Child class inherits properties from parent class.

# 2. Constructor chaining using super()

# 3. Method overriding
# Child method replaces parent method but can still call it.

# 4. Code reuse
# super() allows reuse of parent functionality.



# =============================================================
# SIMPLE RULE TO REMEMBER
# =============================================================

# super() → used to call parent class methods
# especially constructors (__init__)
