class Employee:
    def __init__(self,role,dept,sala):
        self.role=role
        self.dept=dept
        self.sala=sala
    def showdetails(self):
        print("role",self.role,"department=",self.dept,"salary",self.sala)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("SDE","Head",150000)
    def all(self):
        print("name is",self.name,"his age is ", self.age)
        self.showdetails()
E=Engineer("Kondareddy",21)
E.all()