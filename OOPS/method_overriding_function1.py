class konda:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def display(self):
        print("This is the display method of the konda class.")
object=konda("konda", 20)
object.display()  # This will call the second display method, which overrides the first one. The output will be: "This is the display method of the konda class."
# paina code lo manam display method ni rendu sarlu define chesamu, kani second definition first definition ni override chestundi. kabati output lo first display method ni call cheyyadu, second display method matrame call avutundi.