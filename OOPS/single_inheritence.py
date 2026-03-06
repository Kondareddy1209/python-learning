# -----------------------------------------
# Example Program: Single Inheritance
# -----------------------------------------

# Base Class (Parent Class)
class konda:
    
    # Method defined inside the parent class
    def reddy(self):
        # This method prints a message
        print("Kondareddy")


# Derived Class (Child Class)
# This class inherits from the parent class 'konda'
class DerivedClass(konda):
    
    # Method defined inside the child class
    def kondareddy(self):
        # This method prints a message
        print("Ambavaram")


# Creating an object of the child class
# The object can access methods from both the parent and child classes
obj = DerivedClass()

# Calling method from the parent class
# Even though the method is defined in 'konda',
# it can be used because DerivedClass inherits from it
obj.reddy()

# Calling method from the child class
obj.kondareddy()