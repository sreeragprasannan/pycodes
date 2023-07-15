class BaseClass:
    def __init__(self):
        self.name = None
        print("Base init")

    def set_name(self, name):
        self.name = name
        print("Base class set name")


class SubClass(BaseClass):
    # constructor over-riding
    def __init__(self):
        super().__init__() # to prevent constructor over-riding
        print("Subclass init")

    # function over-riding
    def set_name(self, name):
        super().set_name(name)  # to prevent over-riding
        print("Sub class set name")

    def welcome(self):
        print("welcome")

    def display_name(self):
        print("Name: " + self.name)


y = SubClass()
y.welcome()
y.set_name("sreerag")
y.display_name()
