# Parent Class
class konda:
    # Method inside parent class
    def reddy(self):
        # assigning values to instance variables
        self.name = "Konda Reddy"
        self.age = 20


# Child Class inheriting from konda
class DerivedClass(konda):
    
    # New method in child class
    def konda_re(self):
        # assigning value to a new variable
        self.na = "Derived Class Variable"


# issubclass(child_class, parent_class)
# This checks whether DerivedClass is derived from konda

print(issubclass(DerivedClass, konda))  # Expected Output: True