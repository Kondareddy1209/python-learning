# -------------------- CLASS RELATIONSHIP GRAPH --------------------
#
#          Person                Job
#            |                    |
#            |                    |
#            ------> Employee <---
#
# Employee inherits methods from both Person and Job
# This is called MULTIPLE INHERITANCE
# ------------------------------------------------------------------


# Parent Class 1
class Person:
    # Method to set the name
    def konda(self, name):
        self.name = name   # storing name in the object


# Parent Class 2
class Job:
    # Method to set the salary
    def reddy(self, salary):
        self.salary = salary   # storing salary in the object


# Child Class (inherits from Person and Job)
class Employee(Person, Job):

    # Method to display details
    def details(self):
        print(self.name, "earns", self.salary)


# -------------------- PROGRAM FLOW GRAPH --------------------
#
# emp = Employee()
#        |
#        v
# emp.konda("konda")  ---> sets name
#        |
#        v
# emp.reddy(5000)     ---> sets salary
#        |
#        v
# emp.details()       ---> prints output
#
# Object Memory:
# emp
#  ├── name = "konda"
#  └── salary = 5000
# ------------------------------------------------------------


# Creating object
emp = Employee()

# Calling method from Person class
emp.konda("konda")

# Calling method from Job class
emp.reddy(5000)

# Calling Employee class method
emp.details()