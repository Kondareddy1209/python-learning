# Parent Class
class konda:
    
    # Parent class method
    def reddy(self):
        print("This is the Parent class method")


# Child Class inheriting from konda
class DerivedClass(konda):

    # Method with the same name as the parent class method
    # This overrides the parent method
    def reddy(self):
        print("This is the Child class method (Method Overriding)")


# Creating object of child class
obj = DerivedClass()

# Calling method
# Since the child class overrides the method,
# the child method will execute instead of parent method
obj.reddy()


# Checking subclass relationship
print(issubclass(DerivedClass, konda))  # Expected Output: True