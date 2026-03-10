class konda:
    def reddy(self):
        self.name=self.name
        self.age=self.age
class DerivedClass(konda):
    def reddy(self):
        self.na=self.na
print(issubclass(konda,DerivedClass))