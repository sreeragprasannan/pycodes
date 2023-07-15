class First:
    def display(self):
        print("First")

class Second:
    def display(self):
        print("Second")

class Third(First,Second):
    def display_third(self):
        print("third")


x=Third()
x.display_third()
x.display()

print(Third.mro())