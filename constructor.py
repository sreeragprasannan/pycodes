class Members():
    year = 2023

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year: " + str(Members.year))
        print("Name: " + self.name)
        print("age: " + str(self.age))
        print("Place: " + self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1

    @staticmethod
    def display_dash():
        print("_________________________________")


x = Members("Sreerag", 24, "Trissur")
y = Members("Faizal", 25, "Ernakulam")

x.display()
Members.display_dash()
y.display()
Members.display_dash()
Members.year = Members.year + 1
x.add_age()
y.add_age()

x.display()
Members.display_dash()
y.display()
Members.display_dash()
Members.add_year()

x.add_age()
y.add_age()
x.relocate("Bangalore")
y.relocate("Chenni")
x.display()
Members.display_dash()
y.display()
