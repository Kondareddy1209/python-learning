# ------------------ CLASS STRUCTURE (Multiple Inheritance) ------------------
#
#        Person          Job
#          |              |
#          |              |
#           -----> Employee <-----
#
# Employee inherits properties from both Person and Job
# ---------------------------------------------------------------------------


# Parent Class 1
class Person:
    # Constructor to initialize name
    def __init__(self, name):
        self.name = name   # store the name in the object


# Parent Class 2
class Job:
    # Constructor to initialize salary
    def __init__(self, salary):
        self.salary = salary   # store the salary in the object


# Child Class inheriting from both Person and Job
class Employee(Person, Job):

    # Constructor of Employee
    def __init__(self, name, salary):
        # Call constructor of Person to set name
        Person.__init__(self, name)

        # Call constructor of Job to set salary
        Job.__init__(self, salary)

    # Method to display employee details
    def details(self):
        print(self.name, "earns", self.salary)


# ------------------ PROGRAM FLOW ------------------
#
# emp = Employee("Jennifer", 50000)
#        |
#        |-- Person.__init__() → sets name
#        |
#        |-- Job.__init__() → sets salary
#        |
#        v
# emp.details() → prints name and salary
#
# Object Memory:
# emp
#  ├── name = "Jennifer"
#  └── salary = 50000
# --------------------------------------------------


# Create an object of Employee
emp = Employee("Jennifer", 50000)

# Call the method to display details
emp.details()